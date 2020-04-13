#this file puts a comment in front of a line that jena doesn't know how to deal with
#before we ran this file we also ran the sed command in the sed.txt text file otherwise this script would take forever.
$files = Get-ChildItem "D:\yuda\yago\yago3.1_entire_ttl" -Filter *.ttl
foreach ($f in $files)
{
  :label
  while($true)
  {
    $output = riot --validate $f 2> "log.$($f).log"
    Write-Host "*******************************************" 
    (Get-Content "log.$($f).log" ) | Where { $_ } | Set-Content "log.$($f).log"
    $str= Get-Content "log.$($f).log" -Tail 1 
    Remove-Item 'sed*'
    if ($str -like '*ERROR*') 
    { 
      Write-Host "file $($f)"
      Write-Host $str
      $r = [regex] "\[([^\[]*)\]"
      $brackets = $r.match($str)
      Write-Host $brackets
      $number= $brackets -replace '\D+([0-9]*).*','$1' 
      Write-Host $number
      sed -i "$($number)s/.*/#yuda &/" $f
      if ($LastExitCode -ne 0)
      {
        echo "ERROR: "
        echo $output
        return
      }
    }
    else
    {
      Write-Host "file $($f)"
      Move-Item -Path ".\$($f)" -Destination ".\done\$($f)"
      Move-Item -Path ".\log.$($f).log" -Destination ".\done\log.$($f).log"
      break label
    }
  }
}