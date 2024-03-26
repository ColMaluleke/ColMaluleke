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
`If you were in charge of a team of IT Administrators, who would you want in your senior higher-paying position?`
--> Administrators would need several minutes to click their way through a GUI each time they need to perform a task?
--> Or one who can perform tasks in a few seconds, after automating them?
Ask a Cisco Andministrator, or an AS/400 operator, or a Unix Administrator. --> The answer is: "I'd rather have the person who can run things more efficiently from the command-line"
- The world is now split into 2 groups:
    1. Administrators who can use PowerShell
    2. Those who can't
- Your only choice is to learn PowerShell.

# And now, it's just PowerShell
- In mid-2016, Microsoft made PowerShell completely Open-Source. --> It released versions of PowerShell (without Windows attached) for MacOS and numerous Linux builds. Now the same object-centric shell is available on many Operating Systems, and can be evolved and improved by a worldwide community.

# Is this course for you?
- Microsoft's PowerShell team loosely defines 3 audiences who use PowerShell:
    1. Administartors who primarily run commands and consume tools written by others.
    2. Administrators who combine commands and tools into more complex processes, and perhaps package those as tools that less-experienced administrators can use.
    3. Administrators and developers who create reusable tools and applications.
- We think it's valuable for anyone, even a developer, to understand how the shell is used to run commands.
- If you're going to create your own tools and commands, you should know the patterns that the shell uses, as they allow you to make tools and commands that work as well as they can within the shell.
- If you're interested in creating scripts to automate complex processes, such as new provisioning , then you'll see how to do that by the end of this course. --> You'll even see how to get started on creating your own commands that other administrators can use,
- The goal is toget youusing the Shell and being effective with it in a Production Environment. --> We'll also show you a couple of ways to use PowerShell to connect to external management technologies; Windows Management Instrumentation (WMI) and regular expressions are the 2 exmaples that come to mind.
- In short, this course isn't meant to be the last thing you use to learn PowerShell, but instead it's designed to be a great first step.

# Setting uo your lab environment
