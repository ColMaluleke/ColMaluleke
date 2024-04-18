Managing Azure Active Directry Objects
# Criteria:
--> Creating Azure AD users and groups
--> Creating AUs (Administrative Units)
--> Managing user and group properties
--> Managing device settings
--> Perform bulk user updates
--> Cofiguring Azure AD join
--> Configuring SSPR (Self Service Password Reset)

# Creating Azure AD users and groups
Azure AD offers a `directory` and `identity management` solution within the cloud. --> It offers traditional username and password identity management, alongside roles and permissions management.
It offers more enterprise-grade solutions, such as MFA (Multi-Factor Authentication), appliction monitoring, solution monitoring, and alerting.
Azure AD can easily be integrated with your on-prem Active Directory to create a hybrid infrastructure. --> `Azure AD + On-Prem Active Directory = Hybrid`

# Azure AD offers the following Pricing Plans:
Free --> This offers the most basic features such as:
         -- Support for SSO (Single Sign-On) across Azure.
         -- Microsoft 365 and other SaaS (Software as a Service) applications.
         -- Azure B2B (Business to Business) for external users.
         -- Support for Azure AD connect synchronization.
         -- Self-Service Password Change
         -- User and group management
         -- Standard Security Reports
Office 365 Apps --> Specific Office 365 subscriptions also provide some functionality such as:
         -- User and group management
         -- Cloud authentication
         -- Pass-through authentication
         -- Password hash synchronization
         -- Seamless SSO (Single Sign-On)
         -- etc.
Premium 1 (P1) --> This Pricing plan offers:
         -- Advanced repoting
         -- MFA (Multi-Factor Authentication)
         -- Conditional Access
         -- Mobile Device Management (MDM) auto-enrollment
         -- Azure AD Connect Health
         -- Advanced Adminstration, such as:
            -- Dynamic groups
            -- Self-Service group managment
            -- Microsoft Identity Manager
Premium 2 (P2) --> In addition to the  free and P1 features, the Premium 2 license includes:
         -- Azure AD Identity protection
         -- Privileged Identity Management
         -- Access reviews
         -- Entitlement management

# Creating users in Azure AD
To create users in Azure AD, do the following:
1. Navigate to the `Azure Portal`
2. In the left-hand menu, select `Azure Active Directory`
3. Under the `Manage` blade of Azure AD (in the left-hand menu), select `Users|All Users --> The select the `+ New User` option from the menu on top.
4. Fill in the fields:--> Name
                      --> Username  -- The Username is the identifier that users enters to sign into Azure AD. Select your `domain name`, which has been configured, and add it to the end of the username. -- The default is usually an `onmicrosoft.com` domain.
                      --> First Name
                      --> Last Name
5. Leave the section under `Groups and Roles` in the default settings, for now.
6. Next, we need to fill in information regarding the following:
    --> Block Signin: No
    --> Usage Location: South Africa
    --> Job Title Azure Administrator
    --> Department: IT
    --> Company: Citadel
    --> Manager: No manager selected
7. Click `Create`
8. Repeat these steps to create more users.

# Creating groups in Azure AD
There are 2 main group types:
--> `Security groups`: These groups serve the same function as traditional on-prem groups, which is to secure objects within a directory. -- In this case, it is to secure objects within Azure AD.
--> `Microsoft 365 groups`: These groups are used to provide a group of people with access to a collection of shared resources. -- This isn't limited to Azure AD but includes shared mailboxes, calendars, SharePoint Libraries, and other Microsoft 365-related services.

Security groups are used as containers to group users or devices together. There are 3 main membership types for security groups:
1. `Assigned` --> This is where you manually assign users to a group.
2. `Dynamic User` --> This is where you can specify parameters to automatically group users. -- For example, grouping all users who work in a certain department or share a job title.
3. `Dynamic Devices` --> This is where you can specify parameters to automatically group devices. -- For example, grouping all devices that have the same Operating System (OS) version.

To create and manage groups from the Azure AD tenant in the Azure Portal, you have to perform the following steps:
1. Navigate to `Azure Portal`
2. In the left-hand menu, select `Azure Active Directory`
3. Under the manage blade of Azure AD in the left-had menu, select `Groups | All Groups` --> Then select the `+ New group` option on top.
4. Add the following values to create the new group:
    --> Group Type: Security
    --> Group Name: Azure Admins
    --> Group Description: Dynamic group for all Azure Admins
    --> Azure AD Roles Can Be Assigned To The Group: No
    --> Membership Type: Dynamic User
    --> Owners: No Owners Selected
5. [Do more research on adding a dynamic query] --> For this example (for the dynamic query rule), the `property` is Job Title, the `operator' is Equals, and the `value` is Azure Administrator.
6. Click on `Create`

\\Remember that when using dynamic groups, a Premium 1 (P1) license needs to be assigned to the user.\\

Now that the group has been created, replication only takes 5 minutes. --> Refresh the web page, and users will appear as members of the Azure Admins group that was created.