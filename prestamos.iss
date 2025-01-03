; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "sistema prestamos"
#define MyAppVersion "2.5.1"
#define MyAppPublisher "ResOty LIZI, Inc."
#define MyAppURL "https://www.resoty.com/"
#define MyAppExeName "main.exe"
#define MyAppAssocName MyAppName + " File"
#define MyAppAssocExt ".exe"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{B26499BD-58B8-4374-BD2D-AC8C46DFAAB6}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible
ChangesAssociations=yes
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\Astut\Desktop\project\executable\sev_prs
OutputBaseFilename=prestamos setup
SetupIconFile=C:\Users\Astut\Desktop\project\sev_prestamo\img\micro-bank.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\backend.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\banco.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\bd_prestamos.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\caja.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\clientes.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\estado_cuotas.xlsx"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\estilos.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\flotante.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\funcionalidad.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\index.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\ingresos.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\main.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\main.spec"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\movimientos.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\operando.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\prestamo.xlsx"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\prestamos_bd.db"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Astut\Desktop\project\sev_prestamo\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

