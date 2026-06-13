# IAM Role Catalog Extract

Catalog date: 2026-06-07  
Maintainer: Platform Access Operations

## `deploy_operator`

Tier: project operational role  
Typical environments: development, staging  
Capabilities: update deployment metadata, refresh deployment manifests, trigger
project-scoped deployment previews, and read deployment status for the target
project.  
Owner path: project owner or active delegate for the target project and
environment.  
Current queue references: IAM-1401.

## `prod_admin`

Tier: production administrator role  
Typical environments: production  
Capabilities: broad configuration updates, privileged runtime inspection,
production control-plane changes, and access to administrative panels for the
target production project.  
Owner path: production project owner plus the production access review path
listed in the authority matrix. External contractors need the contractor record
and production project owner path to align with the requested resource.  
Current queue references: IAM-1402.

## `serviceAccountTokenCreator`

Tier: service account impersonation role  
Typical environments: production and controlled shared services  
Capabilities: mint short-lived tokens for the target service account and run
actions as that service account within its configured permissions.  
Owner path: project owner or backup owner for the service account project.
Release coordination or change-calendar management is recorded separately from
service account impersonation.  
Current queue references: IAM-1403.

## `diagnostic_export_viewer`

Tier: diagnostics data viewer  
Typical environments: production support and controlled diagnostics projects  
Capabilities: view diagnostic bundle metadata and export references connected
to crash dump analysis for the target project.  
Owner path: diagnostics project owner and data steward for production records,
with partner group identity recorded in the ticket.  
Current queue references: IAM-1404.

## `sandbox_flag_operator`

Tier: sandbox project role  
Typical environments: sandbox  
Capabilities: update sandbox-only preview flags, inspect sandbox flag state,
and refresh build-pipeline flag checks.  
Owner path: sandbox project owner or active sandbox delegate for the target
project.  
Current queue references: IAM-1405.
