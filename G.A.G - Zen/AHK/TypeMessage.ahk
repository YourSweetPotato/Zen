if (A_Args.Length > 0)
{
    messageToType := A_Args[1]
    MouseMove 128, 337
    Sleep 200
    MouseMove 135, 337
    Sleep 200
    MouseMove 128, 337
    Sleep 200
    MouseClick "left"
    Sleep 100
    MouseClick "left"
    Sleep 100
    For i, char in StrSplit(messageToType)
    {
        Send char
        Sleep 50
    }
    SendInput "{Enter}"
}
ExitApp