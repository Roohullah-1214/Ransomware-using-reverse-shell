 invisible.vbs
Set WshShell = CreateObject("WScript.Shell")

' Iterate over all arguments passed to the script
For i = 0 To WScript.Arguments.Count - 1
    WshShell.Run """" & WScript.Arguments(i) & """", 0, False
Next
