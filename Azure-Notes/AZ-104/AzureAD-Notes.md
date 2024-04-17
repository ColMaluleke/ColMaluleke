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