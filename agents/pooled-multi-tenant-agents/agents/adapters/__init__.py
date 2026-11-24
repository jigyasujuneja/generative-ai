# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=line-too-long

"""Live Google Cloud and 3P enterprise connector adapters (`agents.adapters`)."""

from __future__ import annotations

from agents.adapters._bridge_runtime import DEFAULT_BQ_DATASET
from agents.adapters._bridge_runtime import DEFAULT_BQ_TABLE
from agents.adapters._bridge_runtime import DEFAULT_DLP_DEIDENTIFY_TEMPLATE
from agents.adapters._bridge_runtime import DEFAULT_DLP_INSPECT_TEMPLATE
from agents.adapters._bridge_runtime import DEFAULT_FIRESTORE_DB
from agents.adapters._bridge_runtime import DEFAULT_GCP_PROJECT
from agents.adapters._bridge_runtime import DEFAULT_GCP_REGION
from agents.adapters._bridge_runtime import DEFAULT_KMS_KEYRING
from agents.adapters._bridge_runtime import DEFAULT_MODEL_ARMOR_TEMPLATE_ID
from agents.adapters._bridge_runtime import FINVAULT_KMS_KEY
from agents.adapters._bridge_runtime import RETAILSTREAM_KMS_KEY
from agents.adapters._bridge_runtime import ConnectorSecretUnavailableError
from agents.adapters._bridge_runtime import _DotEnvHelper
from agents.adapters._bridge_runtime import _fetch_secret_json
from agents.adapters._bridge_runtime import _legacy_adc_headers
from agents.adapters._bridge_runtime import _tenant_headers
from agents.adapters._bridge_runtime import _tenant_policy
from agents.adapters._bridge_runtime import access_tenant_secret
from agents.adapters._bridge_runtime import is_live_gcp_enabled
from agents.adapters._bridge_runtime import load_live_connector_secret
from agents.adapters.enterprise_connectors import LiveAtlassianJiraConnector
from agents.adapters.enterprise_connectors import LiveMicrosoftEntraOIDCConnector
from agents.adapters.enterprise_connectors import LiveServiceNowITOMConnector
from agents.adapters.guardrails import LiveCloudDLPGuardrail
from agents.adapters.guardrails import LiveModelArmorGuardrail
from agents.adapters.kms_cmek import _KMS_VERIFY_CACHE
from agents.adapters.kms_cmek import _KMS_VERIFY_LOCK
from agents.adapters.kms_cmek import KMS_VERIFY_TTL_SECONDS
from agents.adapters.kms_cmek import LiveCloudKMSCMEKVerifier
from agents.adapters.kms_cmek import clear_kms_verify_cache
from agents.adapters.kms_cmek import evict_kms_verify_cache_for_tenant
from agents.adapters.storage_and_telemetry import LiveBigQueryOTelSink
from agents.adapters.storage_and_telemetry import LiveFirestoreMemoryBank
from agents.adapters.storage_and_telemetry import LiveGCSCMEKRunbookVault
from agents.adapters.storage_and_telemetry import LiveVertexMemoryBankAdapter
from agents.adapters.vertex_runner import LiveADKVertexRunner
from agents.adapters.vertex_runner import LiveGeminiAgentSandboxClient
from agents.adapters.vertex_runner import _get_live_gemini_sandbox_manager

__all__ = [
    "DEFAULT_BQ_DATASET",
    "DEFAULT_BQ_TABLE",
    "DEFAULT_DLP_DEIDENTIFY_TEMPLATE",
    "DEFAULT_DLP_INSPECT_TEMPLATE",
    "DEFAULT_FIRESTORE_DB",
    "DEFAULT_GCP_PROJECT",
    "DEFAULT_GCP_REGION",
    "DEFAULT_KMS_KEYRING",
    "DEFAULT_MODEL_ARMOR_TEMPLATE_ID",
    "FINVAULT_KMS_KEY",
    "KMS_VERIFY_TTL_SECONDS",
    "RETAILSTREAM_KMS_KEY",
    "_KMS_VERIFY_CACHE",
    "_KMS_VERIFY_LOCK",
    "ConnectorSecretUnavailableError",
    "LiveADKVertexRunner",
    "LiveAtlassianJiraConnector",
    "LiveBigQueryOTelSink",
    "LiveCloudDLPGuardrail",
    "LiveCloudKMSCMEKVerifier",
    "LiveFirestoreMemoryBank",
    "LiveGCSCMEKRunbookVault",
    "LiveGeminiAgentSandboxClient",
    "LiveMicrosoftEntraOIDCConnector",
    "LiveModelArmorGuardrail",
    "LiveServiceNowITOMConnector",
    "LiveVertexMemoryBankAdapter",
    "_DotEnvHelper",
    "_fetch_secret_json",
    "_get_live_gemini_sandbox_manager",
    "_legacy_adc_headers",
    "_tenant_headers",
    "_tenant_policy",
    "access_tenant_secret",
    "clear_kms_verify_cache",
    "evict_kms_verify_cache_for_tenant",
    "is_live_gcp_enabled",
    "load_live_connector_secret",
]
