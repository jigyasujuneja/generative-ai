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

# pylint: disable=import-outside-toplevel,line-too-long

"""Cryptographic identity, tenant directory, OBO/DPoP verifier, 3LO vault, and QoS bulkheads."""

from __future__ import annotations

from typing import Any

from agents.auth.dpop import AsymmetricDPoPProvider
from agents.auth.dpop import _b64url_uint
from agents.auth.edge_verifier import _STATE_CLAIM_BINDINGS
from agents.auth.edge_verifier import EdgeAuthVerifier
from agents.auth.edge_verifier import _claim
from agents.auth.edge_verifier import _context_verifier
from agents.auth.edge_verifier import _delegation_tag
from agents.auth.edge_verifier import _normalize_state_value
from agents.auth.edge_verifier import averify_signed_adk_state
from agents.auth.edge_verifier import get_active_envelope
from agents.auth.edge_verifier import propagate_to_subagent
from agents.auth.edge_verifier import verify_signed_adk_state
from agents.auth.envelope import _ACTIVE_TENANT_ENVELOPE
from agents.auth.envelope import _DELEGATION_DEPTH_KEY
from agents.auth.envelope import ContextEnvelope
from agents.auth.envelope import MemoryScope
from agents.auth.envelope import RequestContext
from agents.auth.envelope import SecurityContext
from agents.auth.envelope import SubscriptionTier
from agents.auth.envelope import TenantContext
from agents.auth.envelope import tenant_qualified_user_id
from agents.auth.offboarding import offboard_tenant
from agents.auth.tenant_directory import _BASE_TENANT_DIRECTORY
from agents.auth.tenant_directory import _TENANT_EVICTION_LOCK
from agents.auth.tenant_directory import _TENANT_EVICTION_TARGETS
from agents.auth.tenant_directory import _TENANT_ID_PATTERN
from agents.auth.tenant_directory import PLATFORM_GLOBAL_KEY_ID
from agents.auth.tenant_directory import PLATFORM_GLOBAL_KMS_KEY_NAME
from agents.auth.tenant_directory import ROLE_PLATFORM_SCOPES
from agents.auth.tenant_directory import TENANT_DIRECTORY
from agents.auth.tenant_directory import USER_ROLE_ALLOWED_SCOPES
from agents.auth.tenant_directory import _load_base_tenant_directory
from agents.auth.tenant_directory import register_tenant
from agents.auth.tenant_directory import register_tenant_eviction_target
from agents.auth.tenant_directory import reset_dynamic_tenants
from agents.auth.vault_and_bulkhead import AuthManager3LOVault
from agents.auth.vault_and_bulkhead import Delegated3LOToken
from agents.auth.vault_and_bulkhead import PrefixCacheSimulator
from agents.auth.vault_and_bulkhead import RedisBulkheadStore
from agents.auth.vault_and_bulkhead import RemoteBroker3LOVault
from agents.auth.vault_and_bulkhead import SharedBulkheadStore
from agents.auth.vault_and_bulkhead import TokenBucketBulkhead
from agents.auth.vault_and_bulkhead import _BucketState
from agents.auth.vault_and_bulkhead import build_bulkhead_from_env
from agents.auth.vault_and_bulkhead import build_redis_client_from_env
from agents.auth.vault_and_bulkhead import get_default_3lo_vault
from agents.platform_config import PLATFORM_SCOPES
from agents.platform_config import RESERVED_TENANT_IDS


def __getattr__(name: str) -> Any:
    """Lazy re-export of `MemoryBankPartitioner` to avoid circular imports with `memory_crypto`."""
    if name == "MemoryBankPartitioner":
        from agents.memory_bank import MemoryBankPartitioner

        return MemoryBankPartitioner
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "PLATFORM_GLOBAL_KEY_ID",
    "PLATFORM_GLOBAL_KMS_KEY_NAME",
    "PLATFORM_SCOPES",
    "RESERVED_TENANT_IDS",
    "ROLE_PLATFORM_SCOPES",
    "TENANT_DIRECTORY",
    "USER_ROLE_ALLOWED_SCOPES",
    "_ACTIVE_TENANT_ENVELOPE",
    "_BASE_TENANT_DIRECTORY",
    "_DELEGATION_DEPTH_KEY",
    "_STATE_CLAIM_BINDINGS",
    "_TENANT_EVICTION_LOCK",
    "_TENANT_EVICTION_TARGETS",
    "_TENANT_ID_PATTERN",
    "AsymmetricDPoPProvider",
    "AuthManager3LOVault",
    "ContextEnvelope",
    "Delegated3LOToken",
    "EdgeAuthVerifier",
    "MemoryScope",
    "PrefixCacheSimulator",
    "RedisBulkheadStore",
    "RemoteBroker3LOVault",
    "RequestContext",
    "SecurityContext",
    "SharedBulkheadStore",
    "SubscriptionTier",
    "TenantContext",
    "TokenBucketBulkhead",
    "_BucketState",
    "_b64url_uint",
    "_claim",
    "_context_verifier",
    "_delegation_tag",
    "_load_base_tenant_directory",
    "_normalize_state_value",
    "averify_signed_adk_state",
    "build_bulkhead_from_env",
    "build_redis_client_from_env",
    "get_active_envelope",
    "get_default_3lo_vault",
    "offboard_tenant",
    "propagate_to_subagent",
    "register_tenant",
    "register_tenant_eviction_target",
    "reset_dynamic_tenants",
    "tenant_qualified_user_id",
    "verify_signed_adk_state",
]
