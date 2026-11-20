---
title: "Get audit logs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/audit-logs/get-audit-logs
scraped_at: 2026-11-15T03:40:35.451646
word_count: 694
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

limit

integer

default:10

Number of items to return

Required range: `1 <= x <= 100`

cursor

string | null

Cursor for pagination (base64-encoded JSON string)

workspace\_id

string<uuid> | null

Filter by workspace ID

start\_time

string<date-time>

required

Start datetime (inclusive) in ISO 8601 format

end\_time

string<date-time>

required

End datetime (inclusive) in ISO 8601 format

operations

enum<string>[] | null

Filter by operation names. If omitted, all operations are returned.

Operations that are logged in audit\_logs database table.

Available options:

`create_api_key`,

`delete_api_key`,

`create_personal_access_token`,

`delete_personal_access_token`,

`revoke_personal_access_token`,

`reinstate_personal_access_token`,

`create_service_key`,

`delete_service_key`,

`update_service_key`,

`create_role`,

`update_role`,

`delete_role`,

`upsert_role_restriction`,

`invite_user_to_org`,

`invite_users_to_org_batch`,

`add_basic_auth_users_to_org`,

`update_basic_auth_user`,

`delete_org_pending_member`,

`update_org_pending_member`,

`delete_org_member`,

`update_org_member`,

`create_sso_settings`,

`update_sso_settings`,

`delete_sso_settings`,

`update_default_sso_provision_organization`,

`update_login_methods`,

`create_oidc_integration`,

`update_oidc_integration`,

`delete_oidc_integration`,

`create_oidc_sso_settings`,

`update_oidc_sso_settings`,

`delete_oidc_sso_settings`,

`update_organization_info`,

`update_business_info`,

`update_payment_plan`,

`update_payment_method`,

`create_payment_setup_intent`,

`create_payment_checkout_session`,

`confirm_payment_checkout_session`,

`create_payment_account_link`,

`create_workspace`,

`update_workspace`,

`delete_workspace`,

`add_member_to_workspace`,

`add_members_to_workspace_batch`,

`delete_workspace_member`,

`update_workspace_member`,

`delete_workspace_pending_member`,

`update_workspace_pending_member`,

`read_workspace_encrypted_secrets`,

`update_workspace_secrets`,

`delete_workspace_secret`,

`upsert_workspace_secret`,

`read_org_encrypted_secrets`,

`update_org_secrets`,

`unshare_entities`,

`upsert_slack_app_configuration`,

`delete_slack_app_configuration`,

`upsert_github_app_configuration`,

`update_github_app_configuration`,

`delete_github_app_configuration`,

`upsert_gitlab_connection`,

`delete_gitlab_connection`,

`set_tenant_handle`,

`create_tag_key`,

`update_tag_key`,

`delete_tag_key`,

`create_tag_value`,

`update_tag_value`,

`delete_tag_value`,

`create_tagging`,

`delete_tagging`,

`create_agent`,

`create_agent_environment`,

`update_agent`,

`delete_agent`,

`create_agent_runtime_binding`,

`create_agent_environment_api_key`,

`delete_agent_environment_api_key`,

`create_tracer_session`,

`update_tracer_session`,

`delete_tracer_session`,

`delete_tracer_sessions`,

`delete_runs`,

`share_run`,

`unshare_run`,

`share_thread`,

`unshare_thread`,

`create_dataset`,

`create_csv_dataset`,

`create_experiment_via_upload`,

`create_playground_experiment`,

`create_comparative_experiment`,

`delete_comparative_experiment`,

`delete_dataset`,

`delete_datasets`,

`update_dataset`,

`update_dataset_version`,

`update_dataset_splits`,

`share_dataset`,

`unshare_dataset`,

`clone_dataset`,

`download_dataset`,

`create_example`,

`create_examples`,

`update_example`,

`update_examples`,

`update_examples_metadata`,

`sync_examples`,

`delete_example`,

`delete_examples`,

`create_bulk_export`,

`cancel_bulk_export`,

`read_bulk_export_destination`,

`create_bulk_export_destination`,

`update_bulk_export_destination`,

`delete_bulk_export_destination`,

`update_ttl_settings`,

`update_usage_limit`,

`delete_usage_limit`,

`create_model_price_map`,

`update_model_price_map`,

`delete_model_price_map`,

`create_chart`,

`update_chart`,

`delete_chart`,

`create_chart_section`,

`update_chart_section`,

`delete_chart_section`,

`clone_chart_section`,

`create_org_chart`,

`update_org_chart`,

`delete_org_chart`,

`create_org_chart_section`,

`update_org_chart_section`,

`delete_org_chart_section`,

`create_prompt_webhook`,

`update_prompt_webhook`,

`delete_prompt_webhook`,

`test_prompt_webhook`,

`create_deployment`,

`update_deployment`,

`delete_deployment`,

`cancel_deployment_runs`,

`create_access_policy`,

`delete_access_policy`,

`list_access_policies`,

`read_access_policy`,

`update_access_policy`,

`attach_access_policies`,

`detach_access_policies`,

`read_role_access_policies`,

`read_team_access_policies`,

`create_team`,

`update_team`,

`delete_team`,

`add_team_members`,

`attach_team_access_policy`,

`detach_team_access_policy`,

`remove_team_member`,

`create_team_workspace_grant`,

`update_team_workspace_grant`,

`delete_team_workspace_grant`,

`create_scim_token`,

`update_scim_token`,

`delete_scim_token`,

`create_scim_user`,

`update_scim_user`,

`delete_scim_user`,

`create_scim_group`,

`update_scim_group`,

`delete_scim_group`,

`create_prompt_canvas_quick_action`,

`update_prompt_canvas_quick_action`,

`delete_prompt_canvas_quick_action`,

`create_fleet_usage_limit`,

`update_fleet_usage_limit`,

`delete_fleet_usage_limit`,

`update_credential`,

`delete_credential`,

`create_experiment_view_override`,

`update_experiment_view_override`,

`delete_experiment_view_override`,

`create_alert_rule`,

`update_alert_rule`,

`delete_alert_rule`,

`test_alert_rule`,

`create_forge_configuration`,

`update_forge_configuration`,

`delete_forge_configuration`,

`trigger_forge_configuration`,

`add_annotation_queue_reviewer`,

`remove_annotation_queue_reviewer`,

`create_custom_view`,

`update_custom_view`,

`delete_custom_view`,

`add_items_to_annotation_queue`,

`delete_annotation_queue_item`,

`update_annotation_queue_item`,

`get_annotation_queue_items`,

`submit_nps_response`,

`submit_product_feedback`,

`update_trace_flight_score`,

`create_mcp_server`,

`update_mcp_server`,

`delete_mcp_server`,

`register_mcp_server_oauth`,

`create_mcp_credential_session`,

`invoke_mcp_server`,

`invoke_mcp_gateway`,

`create_mcp_gateway`,

`update_mcp_gateway`,

`delete_mcp_gateway`,

`refresh_mcp_gateway_tools`,

`update_mcp_oidc_connection`,

`delete_mcp_oidc_connection`,

`create_mcp_profile`,

`update_mcp_profile`,

`delete_mcp_profile`,

`create_agent_policy`,

`update_agent_policy`,

`delete_agent_policy`,

`create_credential`,

`read_credential_secret`,

`read_credential_oauth2`,

`create_oauth_provider`,

`update_oauth_provider`,

`delete_oauth_provider`,

`start_oauth_connection`,

`start_agent_auth_secret_input`,

`create_agent_auth_connection`,

`update_agent_auth_connection`,

`delete_agent_auth_connection`,

`update_agent_auth_app`,

`delete_agent_auth_app`,

`create_agent_auth_oidc_integration`,

`update_agent_auth_oidc_integration`,

`delete_agent_auth_oidc_integration`,

`resolve_agent_auth_agent`,

`create_agent_auth_app`,

`create_tool`,

`update_tool`,

`delete_tool`,

`create_connection`,

`update_connection`,

`delete_connection`,

`create_mcp_vendor_settings`,

`update_mcp_vendor_settings`,

`delete_mcp_vendor_settings`,

`create_evaluator`,

`update_evaluator`,

`delete_evaluator`,

`bulk_delete_evaluators`,

`test_evaluator`,

`upsert_feature_default_model`,

`delete_feature_default_model`,

`upsert_feature_disabled_model`,

`delete_feature_disabled_model`,

`create_fleet_webhook`,

`update_fleet_webhook`,

`delete_fleet_webhook`,

`test_fleet_webhook`,

`create_webhook_destination`,

`update_webhook_destination`,

`delete_webhook_destination`,

`test_webhook_destination`,

`create_commit`,

`create_hub_environment`,

`update_hub_environment`,

`delete_hub_environment`,

`create_directory_commit`,

`delete_directory`,

`create_gateway_policy`,

`update_gateway_policy`,

`delete_gateway_policy`,

`invoke_gateway`,

`purchase_prepaid_gateway_provider_credits`,

`create_sandbox_proxy_profile`,

`update_sandbox_proxy_profile`,

`delete_sandbox_proxy_profile`,

`create_sandbox_policy`,

`update_sandbox_policy`,

`delete_sandbox_policy`,

`create_computer_environment`,

`update_computer_environment`,

`archive_computer_environment`,

`update_fleet_feedback`,

`delete_fleet_feedback`,

`list_sandbox_claims`,

`get_sandbox_claim`,

`get_sandbox_claim_status`,

`create_sandbox_claim`,

`update_sandbox_claim`,

`delete_sandbox_claim`,

`batch_delete_sandbox_claims`,

`start_sandbox_claim`,

`stop_sandbox_claim`,

`generate_sandbox_service_url`,

`generate_sandbox_download_url`,

`capture_sandbox_snapshot`,

`list_sandbox_snapshots`,

`get_sandbox_snapshot`,

`create_sandbox_snapshot`,

`delete_sandbox_snapshot`,

`list_sandbox_volumes`,

`get_sandbox_volume`,

`create_sandbox_volume`,

`clone_sandbox_volume`,

`update_sandbox_volume`,

`delete_sandbox_volume`,

`list_sandbox_registries`,

`get_sandbox_registry`,

`create_sandbox_registry`,

`update_sandbox_registry`,

`delete_sandbox_registry`,

`list_sandbox_functions`,

`get_sandbox_function`,

`create_sandbox_function`,

`update_sandbox_function`,

`deploy_sandbox_function`,

`delete_sandbox_function`,

`generate_sandbox_function_token`,

`create_data_plane`,

`delete_data_plane`,

`update_data_plane`,

`create_annotation_queue`,

`populate_annotation_queue`,

`delete_annotation_queue`,

`delete_annotation_queues`,

`update_annotation_queue`,

`add_runs_to_annotation_queue`,

`export_annotation_queue`,

`update_annotation_queue_run`,

`delete_annotation_queue_run`,

`delete_annotation_queue_runs`,

`create_annotation_queue_run_status`,

`create_annotation_queue_item_status`,

`login`,

`send_sso_email_confirmation`,

`confirm_sso_user_email`,

`execute_custom_code`,

`generate_dataset`,

`evaluate_experiment`,

`create_feedback_formula`,

`update_feedback_formula`,

`delete_feedback_formula`,

`create_feedback_config`,

`update_feedback_config`,

`delete_feedback_config`,

`invalidate_mcp_tools_cache`,

`mcp_proxy`,

`create_onboarding_state`,

`update_onboarding_state`,

`create_organization`,

`delete_pending_organization_invite`,

`claim_pending_organization_invite`,

`create_playground_settings`,

`update_playground_settings`,

`delete_playground_settings`,

`create_service_account`,

`delete_service_account`,

`create_tenant`,

`create_filter_view`,

`update_filter_view`,

`rename_filter_view`,

`delete_filter_view`,

`create_insights_job`,

`create_insights_job_config`,

`update_insights_job_config`,

`delete_insights_job_config`,

`update_insights_job`,

`delete_insights_job`,

`read_charts`,

`read_chart_preview`,

`read_chart`,

`read_chart_section`,

`validate_example`,

`validate_examples`,

`read_shared_delta`,

`read_shared_delta_stream`,

`generate_shared_dataset_query`,

`generate_runs_query`,

`read_tracing_dashboard`,

`generate_insights_job_config`,

`read_dataset_delta`,

`delete_pending_workspace_invite`,

`claim_pending_workspace_invite`,

`list_annotation_queues`,

`get_annotation_queue`,

`get_annotation_queue_runs`,

`get_annotation_queue_run`,

`get_annotation_queues_for_run`,

`get_annotation_queue_size`,

`get_annotation_queue_archived_size`,

`get_annotation_queue_total_size`,

`resolve_annotation_queue_run`,

`get_audit_logs`,

`get_sso_settings`,

`list_bulk_exports`,

`list_bulk_export_destinations`,

`get_bulk_export`,

`get_bulk_export_runs`,

`get_bulk_export_run`,

`get_bulk_export_runs_filtered`,

`list_chart_sections`,

`get_dataset_versions`,

`diff_dataset_versions`,

`get_dataset_version`,

`read_dataset_share_state`,

`count_examples`,

`list_feedback_formulas`,

`get_feedback_formula`,

`list_feedback_configs`,

`get_mcp_tools`,

`mcp_proxy_get`,

`get_onboarding_state`,

`read_model_price_map`,

`list_organizations`,

`get_organization_info`,

`get_organization_billing_info`,

`get_org_dashboard`,

`get_company_info`,

`list_organization_roles`,

`list_permissions`,

`list_pending_organization_invites`,

`list_org_members`,

`get_org_usage`,

`get_granular_usage_traces`,

`export_granular_usage_traces_csv`,

`get_granular_usage_deployments`,

`export_granular_usage_deployments_csv`,

`export_usage_backfill_csv`,

`get_login_methods`,

`get_sso_settings_current`,

`list_org_service_keys`,

`list_org_personal_access_tokens`,

`list_all_org_personal_access_tokens`,

`list_service_accounts`,

`list_filter_views`,

`get_filter_view`,

`list_insights_jobs`,

`list_insights_job_configs`,

`get_insights_job`,

`get_insights_job_runs`,

`get_run_cluster`,

`get_usage_limits`,

`get_org_usage_limits`,

`list_workspaces`,

`list_pending_workspace_invites`,

`get_workspace_stats`,

`list_workspace_members`,

`get_shared_tokens`,

`get_workspace_usage_limits_info`,

`list_tag_keys`,

`get_tag_key`,

`list_tag_values`,

`get_tag_value`,

`list_tags`,

`list_tags_for_resource`,

`list_taggings`,

`get_shared_examples_count`,

`list_examples`,

`get_example`,

`get_experiment_view_overrides`,

`get_experiment_view_override`,

`get_dataset_comparison_view`,

`stream_dataset_comparison_view`,

`stream_feedback_delta`,

`read_comparative_experiments`,

`stream_grouped_experiments`,

`get_run_url`,

`query_run`,

`query_runs`,

`batch_query_runs`,

`query_trace`,

`query_traces`,

`query_trace_messages`,

`batch_query_trace_messages`,

`query_thread_messages`,

`query_single_thread_stats`,

`query_thread_stats`,

`query_thread_traces`,

`query_threads`,

`list_github_thread_outcomes`,

`query_github_thread_outcomes`,

`list_pairwise_queues`,

`get_pairwise_queue`,

`list_pairwise_entries`,

`read_run`,

`read_runs`,

`read_example`,

`read_examples`,

`read_feedback`,

`read_feedbacks`,

`create_license_share_link`,

`create_provisioned_saas_org`,

`mint_self_hosted_license`,

`invite_provisioned_org_member`,

`create_self_hosted_customer`,

`update_self_hosted_customer`,

`update_self_hosted_license`,

`get_self_hosted_customer`,

`get_provisioned_saas_org`,

`update_provisioned_saas_org`,

`create_oauth_client`,

`update_oauth_client`,

`delete_oauth_client`,

`rotate_oauth_client_secret`,

`revoke_oauth_grant`,

`create_custom_app`,

`update_custom_app`,

`delete_custom_app`,

`bulk_delete_custom_apps`,

`update_custom_app_share`,

`update_custom_app_claim`,

`download_custom_app_source`,

`create_custom_app_editing_credential`,

`create_custom_app_editing_sandbox`,

`delete_custom_app_editing_sandbox`,

`create_taskset`,

`update_taskset`,

`delete_taskset`,

`create_taskset_version`,

`download_taskset_bundle`,

`create_taskset_task`,

`create_taskset_task_version`,

`delete_taskset_task`,

`get_taskset_task_file_content`,

`create_taskset_world`,

`create_taskset_world_version`,

`get_taskset_world_file_content`,

`create_taskset_run`,

`cancel_taskset_run`,

`test_op_generic`

actor\_ls\_user\_ids

string<uuid>[] | null

Filter by human actor (ls\_user\_id).

actor\_api\_key\_ids

string<uuid>[] | null

Filter by API key actor (api\_key\_id).

resource\_ids

string[] | null

Filter by resource ID. Matches if any resource ID is present on the log.

#### Response

200

application/json

Successful Response

Response model for listing audit logs in OCSF format with pagination.

cursor

string | null

required

items

OCSFApiActivity · object[]

required

Show child attributes