# PowerShell Notes
- Version 1 was released in 2006.
- Most of the people using the shell back then were experienced VBScript users, and they were eager to apply their VBScipt skills to learn PowerShell.
- PowerShell isn't a scripting language. --> It's a command-line shell where you run commande-line utilities. Like all good shells, it has scripting capabilities, but you don't have to use them and you certainly don't have to start with them,

# Why you can't afford to ignore PowerShell
- Let's face it, Windows PowerShell isn't exactly Microsoft's (or anyone else's) first effort at providing automation capabilities to Windows administrators.

# Life without PowerShell
- Windows administrators have always been happy to click around in the GUI to accomplish their tasks.
- GUIs are great because they enable you to discover what you can do.
- Unfortunately, GUIs have no ROI (Return On Investment). If it takes you 5 minutes to create a new user in the Active Directory (and I'm assuming you're filling in a lot of the fields manually), you'll never get any faster than that.
- Jeffrey Snover, the architect of PowerShell call this the "The Last Mile." --> You can do a lot with VBScript (and other similar technologies), but it tends to let you down at some point, never getting you through that last mile to the finish line.

# Life with PowerShell
- Microsoft's goal for PowerShell is to build 100% of a product's administrative functionality in the shell. --> Micrsoft continues to build GUI consoles, but those consoles are executing PowerShell commands behind the scenes.
- Every possible thing you can do with the product is accessible through the shell. --> If you need to automate repetitive tasks or create a process that the GUI doesn't enable well, you can drop into the shell and take full control.
- Several Microsoft products have already adopted this approach, including Exchange Server 2007 and beyond, SharePoint Server 2010 and later, many of the Systen Center products, Office 365, and many components of Windows itself.
- Windows Server 2012, where PowerShell ver. 3 was introduced, is almost completely managed from PowerShell - or by GUI sitting on top of PowerShell.
- It's already become the foundation for numerous higher-level technologies, including Desired State Configuration (DSC), PowerShell Workflow, and much more. --> PowerShell is everywhere.