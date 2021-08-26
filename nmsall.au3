#RequireAdmin
#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Icon=..\..\..\IconPacks\iconfinder_Magnifier_98917.ico
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
#include <AutoItConstants.au3>
#include <MsgBoxConstants.au3>


While 1
	sleep(1000)
	If WinActivate("GPON NMS") Then
		MsgBox($MB_OK, "", "Sudah siap huaweinya ?", 15)
		BlockInput(1)
		Run('C:\Users\Sandr\Dropbox\Autoit\Desktop\progreshw.exe')
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","!i")
		sleep(1000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","{TAB 2}")
		Sleep(1000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","a")
		Sleep(1000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","!f")
		Sleep(1000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","!o")
		Sleep(7000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","!i")
		Sleep(1000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","!f")
		Sleep(1000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","!o")
		Sleep(15000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","{TAB 3}")
		Sleep(1000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","^a")
		Sleep(1000)
	EndIf
	If WinActivate("GPON NMS") Then
		$hWndd = WinWait("GPON NMS","", 2)
		ControlFocus($hWndd, "", "")
		ControlSend($hWndd, "", "","^c")
		Sleep(3000)
		$hFO = FileOpen("C:\Users\Sandr\Documents\hasiluncfg.txt", 2)
		FileWrite($hFO, "")
		FileClose($hFO)
		FileWrite('C:\Users\Sandr\Documents\hasiluncfg.txt',ClipGet() & @CRLF)
		MsgBox($MB_SYSTEMMODAL, "", "Alhamdulillah done write uncfg huawei", 1)
		ClipPut('')
		;WinSetState ($hWndd, "", @SW_MINIMIZE)
	EndIf
	sleep(1000)
	If WinActivate("Unauthenticated ONU Configuration 1") Then
		$hWndd = WinWait("Unauthenticated ONU Configuration 1","", 2)
		Sleep(2000)
		ControlSend($hWndd, "", "","!r")
		;WinSetState ($hWndd, "", @SW_MINIMIZE)
	EndIf
	sleep(1000)
	If WinActivate("Unauthenticated ONU Configuration 2") Then
		$hWnddd = WinWait("Unauthenticated ONU Configuration 2","", 2)
		Sleep(2000)
		ControlSend($hWnddd, "", "","!r")
		Sleep(1000)
		Run('C:\Users\Sandr\Dropbox\Autoit\Desktop\progresload.exe')
		BlockInput(0)
		;WinSetState ($hWnddd, "", @SW_MINIMIZE)
	EndIf
	sleep(120000)
	BlockInput(1)
	If WinActivate("Unauthenticated ONU Configuration 1") Then
		$hWndd = WinWait("Unauthenticated ONU Configuration 1","", 2)
		ControlSend($hWndd, "", "","{TAB 9}")
		sleep(2000)
	EndIf
	If WinActivate("Unauthenticated ONU Configuration 1") Then
		$hWndd = WinWait("Unauthenticated ONU Configuration 1","", 2)
		ControlSend($hWndd, "", "","^a")
		sleep(2000)
	EndIf
	If WinActivate("Unauthenticated ONU Configuration 1") Then
		$hWndd = WinWait("Unauthenticated ONU Configuration 1","", 2)
		ControlSend($hWndd, "", "","^c")
		sleep(2000)
		$hFO = FileOpen("C:\Users\Sandr\Documents\hasiluncfgZTE.txt", 2)
		FileWrite($hFO, "")
		FileClose($hFO)
		FileWrite('C:\Users\Sandr\Documents\hasiluncfgZTE.txt',ClipGet() & @CRLF)
		ClipPut('')
		;WinSetState ($hWndd, "", @SW_MINIMIZE)
	EndIf
	sleep(2000)
	If WinActivate("Unauthenticated ONU Configuration 2") Then
		$hWnddd = WinWait("Unauthenticated ONU Configuration 2","", 2)
		ControlSend($hWnddd, "", "","{TAB 9}")
		sleep(2000)
	EndIf
	If WinActivate("Unauthenticated ONU Configuration 2") Then
		$hWnddd = WinWait("Unauthenticated ONU Configuration 2","", 2)
		ControlSend($hWnddd, "", "","^a")
		sleep(2000)
	EndIf
	If WinActivate("Unauthenticated ONU Configuration 2") Then
		$hWnddd = WinWait("Unauthenticated ONU Configuration 2","", 2)
		ControlSend($hWnddd, "", "","^c")
		sleep(2000)
		FileWrite('C:\Users\Sandr\Documents\hasiluncfgZTE.txt',ClipGet() & @CRLF)
		MsgBox($MB_SYSTEMMODAL, "", "Alhamdulillah done write uncfg zte", 1)
		ClipPut('')
		BlockInput(0)
		;WinSetState ($hWnddd, "", @SW_MINIMIZE)
	EndIf
	Sleep(895000)
	Example()
WEnd


Example()
Func Example()
    ; Display a progress bar window.
    ProgressOn("Progress Meter", "Harap tunggu proses load uncfg...", "0%", -1, -1, BitOR($WINDOWS_ONTOP, $DLG_MOVEABLE))

    ; Update the progress value of the progress bar window every second.
    For $i = 100 To 0 Step -1
        Sleep(50)
        ProgressSet($i, $i & "%")
    Next

    ; Set the "subtext" and "maintext" of the progress bar window.
    ProgressSet(0, "Done", "Complete ready to start")
    Sleep(1000)

    ; Close the progress window.
    ProgressOff()
EndFunc   ;==>Example


