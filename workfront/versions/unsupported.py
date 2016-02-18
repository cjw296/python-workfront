# generated from https://api-cl01.attask-ondemand.com/attask/api/unsupported/metadata
from ..meta import APIVersion, Object, Field, Reference, Collection

api = APIVersion('unsupported')


class AccessLevel(Object):
    code = 'ACSLVL'
    access_restrictions = Field('accessRestrictions')
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    display_access_type = Field('displayAccessType')
    ext_ref_id = Field('extRefID')
    field_access_privileges = Field('fieldAccessPrivileges')
    is_admin = Field('isAdmin')
    is_unsupported_worker_license = Field('isUnsupportedWorkerLicense')
    last_updated_by_id = Field('lastUpdatedByID')
    last_updated_date = Field('lastUpdatedDate')
    legacy_access_level_id = Field('legacyAccessLevelID')
    license_type = Field('licenseType')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    rank = Field('rank')
    security_model_type = Field('securityModelType')
    app_global = Reference('appGlobal')
    customer = Reference('customer')
    last_updated_by = Reference('lastUpdatedBy')
    access_level_permissions = Collection('accessLevelPermissions')
    access_rule_preferences = Collection('accessRulePreferences')
    access_scope_actions = Collection('accessScopeActions')

    def calculate_sharing(self, obj_code=None, obj_id=None):
        """
        The ``calculateSharing`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/calculateSharing', params)
        

    def clear_access_rule_preferences(self, obj_code=None):
        """
        The ``clearAccessRulePreferences`` action.
        
        :param obj_code: objCode (type: ``string``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        data = self.session.put(self.api_url()+'/clearAccessRulePreferences', params)
        

    def create_unsupported_worker_access_level_for_testing(self):
        """
        The ``createUnsupportedWorkerAccessLevelForTesting`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/createUnsupportedWorkerAccessLevelForTesting', params)
        

    def filter_actions_for_external(self, obj_code=None, action_types=None):
        """
        The ``filterActionsForExternal`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param action_types: actionTypes (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if action_types is not None: params['actionTypes'] = action_types
        data = self.session.put(self.api_url()+'/filterActionsForExternal', params)
        return data['result']

    def filter_available_actions(self, user_id=None, obj_code=None, action_types=None):
        """
        The ``filterAvailableActions`` action.
        
        :param user_id: userID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param action_types: actionTypes (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if obj_code is not None: params['objCode'] = obj_code
        if action_types is not None: params['actionTypes'] = action_types
        data = self.session.put(self.api_url()+'/filterAvailableActions', params)
        return data['result']

    def get_access_level_permissions_for_obj_code(self, obj_code=None, access_level_ids=None):
        """
        The ``getAccessLevelPermissionsForObjCode`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param access_level_ids: accessLevelIDs (type: ``string[]``)
        :return: ``map``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if access_level_ids is not None: params['accessLevelIDs'] = access_level_ids
        data = self.session.put(self.api_url()+'/getAccessLevelPermissionsForObjCode', params)
        return data['result']

    def get_default_access_permissions(self, license_type=None):
        """
        The ``getDefaultAccessPermissions`` action.
        
        :param license_type: licenseType (type: ``com.attask.common.constants.LicenseTypeEnum``)
        :return: ``map``
        """
        params = {}
        if license_type is not None: params['licenseType'] = license_type
        data = self.session.put(self.api_url()+'/getDefaultAccessPermissions', params)
        return data['result']

    def get_default_access_rule_preferences(self):
        """
        The ``getDefaultAccessRulePreferences`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDefaultAccessRulePreferences', params)
        return data['result']

    def get_default_forbidden_actions(self, obj_code=None, obj_id=None):
        """
        The ``getDefaultForbiddenActions`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :return: ``map``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/getDefaultForbiddenActions', params)
        return data['result']

    def get_maximum_access_permissions(self, license_type=None):
        """
        The ``getMaximumAccessPermissions`` action.
        
        :param license_type: licenseType (type: ``com.attask.common.constants.LicenseTypeEnum``)
        :return: ``map``
        """
        params = {}
        if license_type is not None: params['licenseType'] = license_type
        data = self.session.put(self.api_url()+'/getMaximumAccessPermissions', params)
        return data['result']

    def get_security_parent_ids(self, obj_code=None, obj_id=None):
        """
        The ``getSecurityParentIDs`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :return: ``map``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/getSecurityParentIDs', params)
        return data['result']

    def get_security_parent_obj_code(self, obj_code=None, obj_id=None):
        """
        The ``getSecurityParentObjCode`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/getSecurityParentObjCode', params)
        return data['result']

    def get_user_accessor_ids(self, user_id=None):
        """
        The ``getUserAccessorIDs`` action.
        
        :param user_id: userID (type: ``string``)
        :return: ``string[]``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/getUserAccessorIDs', params)
        return data['result']

    def get_viewable_object_obj_codes(self):
        """
        The ``getViewableObjectObjCodes`` action.
        
        :return: ``string[]``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getViewableObjectObjCodes', params)
        return data['result']

    def has_any_access(self, obj_code=None, action_type=None):
        """
        The ``hasAnyAccess`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param action_type: actionType (type: ``com.attask.common.constants.ActionTypeEnum``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if action_type is not None: params['actionType'] = action_type
        data = self.session.put(self.api_url()+'/hasAnyAccess', params)
        return data['result']

    def has_reference(self, ids=None):
        """
        The ``hasReference`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/hasReference', params)
        return data['result']

    def legacy_diagnostics(self):
        """
        The ``legacyDiagnostics`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/legacyDiagnostics', params)
        return data['result']

    def set_access_rule_preferences(self, access_rule_preferences=None):
        """
        The ``setAccessRulePreferences`` action.
        
        :param access_rule_preferences: accessRulePreferences (type: ``string[]``)
        """
        params = {}
        if access_rule_preferences is not None: params['accessRulePreferences'] = access_rule_preferences
        data = self.session.put(self.api_url()+'/setAccessRulePreferences', params)
        

api.register(AccessLevel)


class AccessLevelPermissions(Object):
    code = 'ALVPER'
    access_level_id = Field('accessLevelID')
    core_action = Field('coreAction')
    customer_id = Field('customerID')
    forbidden_actions = Field('forbiddenActions')
    is_admin = Field('isAdmin')
    obj_obj_code = Field('objObjCode')
    secondary_actions = Field('secondaryActions')
    access_level = Reference('accessLevel')
    customer = Reference('customer')

api.register(AccessLevelPermissions)


class AccessRequest(Object):
    code = 'ACSREQ'
    action = Field('action')
    auto_generated = Field('autoGenerated')
    auto_share_action = Field('autoShareAction')
    customer_id = Field('customerID')
    granter_id = Field('granterID')
    last_remind_date = Field('lastRemindDate')
    last_update_date = Field('lastUpdateDate')
    message = Field('message')
    request_date = Field('requestDate')
    requested_obj_code = Field('requestedObjCode')
    requested_obj_id = Field('requestedObjID')
    requested_object_name = Field('requestedObjectName')
    requestor_id = Field('requestorID')
    status = Field('status')
    customer = Reference('customer')
    granter = Reference('granter')
    requestor = Reference('requestor')
    awaiting_approvals = Collection('awaitingApprovals')

    def grant_access(self, access_request_id=None, action_type=None, forbidden_actions=None):
        """
        The ``grantAccess`` action.
        
        :param access_request_id: accessRequestID (type: ``string``)
        :param action_type: actionType (type: ``string``)
        :param forbidden_actions: forbiddenActions (type: ``string[]``)
        """
        params = {}
        if access_request_id is not None: params['accessRequestID'] = access_request_id
        if action_type is not None: params['actionType'] = action_type
        if forbidden_actions is not None: params['forbiddenActions'] = forbidden_actions
        data = self.session.put(self.api_url()+'/grantAccess', params)
        

    def grant_object_access(self, obj_code=None, id=None, accessor_id=None, action_type=None, forbidden_actions=None):
        """
        The ``grantObjectAccess`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param id: id (type: ``string``)
        :param accessor_id: accessorID (type: ``string``)
        :param action_type: actionType (type: ``string``)
        :param forbidden_actions: forbiddenActions (type: ``string[]``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if id is not None: params['id'] = id
        if accessor_id is not None: params['accessorID'] = accessor_id
        if action_type is not None: params['actionType'] = action_type
        if forbidden_actions is not None: params['forbiddenActions'] = forbidden_actions
        data = self.session.put(self.api_url()+'/grantObjectAccess', params)
        

    def ignore(self, access_request_id=None):
        """
        The ``ignore`` action.
        
        :param access_request_id: accessRequestID (type: ``string``)
        """
        params = {}
        if access_request_id is not None: params['accessRequestID'] = access_request_id
        data = self.session.put(self.api_url()+'/ignore', params)
        

    def recall(self, access_request_id=None):
        """
        The ``recall`` action.
        
        :param access_request_id: accessRequestID (type: ``string``)
        """
        params = {}
        if access_request_id is not None: params['accessRequestID'] = access_request_id
        data = self.session.put(self.api_url()+'/recall', params)
        

    def remind(self, access_request_id=None):
        """
        The ``remind`` action.
        
        :param access_request_id: accessRequestID (type: ``string``)
        """
        params = {}
        if access_request_id is not None: params['accessRequestID'] = access_request_id
        data = self.session.put(self.api_url()+'/remind', params)
        

    def request_access(self, obj_code=None, obj_id=None, requestee_id=None, core_action=None, message=None):
        """
        The ``requestAccess`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :param requestee_id: requesteeID (type: ``string``)
        :param core_action: coreAction (type: ``com.attask.common.constants.ActionTypeEnum``)
        :param message: message (type: ``string``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        if requestee_id is not None: params['requesteeID'] = requestee_id
        if core_action is not None: params['coreAction'] = core_action
        if message is not None: params['message'] = message
        data = self.session.put(self.api_url()+'/requestAccess', params)
        

api.register(AccessRequest)


class AccessRule(Object):
    code = 'ACSRUL'
    accessor_id = Field('accessorID')
    accessor_obj_code = Field('accessorObjCode')
    ancestor_id = Field('ancestorID')
    ancestor_obj_code = Field('ancestorObjCode')
    core_action = Field('coreAction')
    customer_id = Field('customerID')
    forbidden_actions = Field('forbiddenActions')
    is_inherited = Field('isInherited')
    secondary_actions = Field('secondaryActions')
    security_obj_code = Field('securityObjCode')
    security_obj_id = Field('securityObjID')
    customer = Reference('customer')

api.register(AccessRule)


class AccessRulePreference(Object):
    code = 'ARPREF'
    access_level_id = Field('accessLevelID')
    accessor_id = Field('accessorID')
    accessor_obj_code = Field('accessorObjCode')
    core_action = Field('coreAction')
    customer_id = Field('customerID')
    forbidden_actions = Field('forbiddenActions')
    secondary_actions = Field('secondaryActions')
    security_obj_code = Field('securityObjCode')
    template_id = Field('templateID')
    user_id = Field('userID')
    access_level = Reference('accessLevel')
    customer = Reference('customer')
    template = Reference('template')
    user = Reference('user')

api.register(AccessRulePreference)


class AccessScope(Object):
    code = 'ACSCP'
    allow_non_view_external = Field('allowNonViewExternal')
    allow_non_view_hd = Field('allowNonViewHD')
    allow_non_view_review = Field('allowNonViewReview')
    allow_non_view_ts = Field('allowNonViewTS')
    allow_non_view_team = Field('allowNonViewTeam')
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    display_order = Field('displayOrder')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    scope_expression = Field('scopeExpression')
    scope_obj_code = Field('scopeObjCode')
    app_global = Reference('appGlobal')
    customer = Reference('customer')

api.register(AccessScope)


class AccessScopeAction(Object):
    code = 'ASCPAT'
    access_level_id = Field('accessLevelID')
    access_scope_id = Field('accessScopeID')
    actions = Field('actions')
    customer_id = Field('customerID')
    scope_obj_code = Field('scopeObjCode')
    access_level = Reference('accessLevel')
    access_scope = Reference('accessScope')
    customer = Reference('customer')

api.register(AccessScopeAction)


class AccessToken(Object):
    code = 'ACSTOK'
    action = Field('action')
    calendar_id = Field('calendarID')
    customer_id = Field('customerID')
    document_id = Field('documentID')
    document_request_id = Field('documentRequestID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    expire_date = Field('expireDate')
    ref_obj_code = Field('refObjCode')
    ref_obj_id = Field('refObjID')
    token_type = Field('tokenType')
    user_id = Field('userID')
    value = Field('value')
    calendar = Reference('calendar')
    customer = Reference('customer')
    document = Reference('document')
    document_request = Reference('documentRequest')
    entered_by = Reference('enteredBy')
    user = Reference('user')

api.register(AccessToken)


class AccountRep(Object):
    code = 'ACNTRP'
    admin_level = Field('adminLevel')
    description = Field('description')
    email_addr = Field('emailAddr')
    ext_ref_id = Field('extRefID')
    first_name = Field('firstName')
    is_active = Field('isActive')
    last_name = Field('lastName')
    password = Field('password')
    phone_number = Field('phoneNumber')
    reseller_id = Field('resellerID')
    ui_code = Field('uiCode')
    username = Field('username')
    reseller = Reference('reseller')

api.register(AccountRep)


class Acknowledgement(Object):
    code = 'ACK'
    acknowledgement_type = Field('acknowledgementType')
    customer_id = Field('customerID')
    entry_date = Field('entryDate')
    owner_id = Field('ownerID')
    reference_object_name = Field('referenceObjectName')
    target_id = Field('targetID')
    customer = Reference('customer')
    owner = Reference('owner')
    target = Reference('target')

    def acknowledge(self, obj_code=None, obj_id=None):
        """
        The ``acknowledge`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/acknowledge', params)
        return data['result']

    def acknowledge_many(self, obj_code_ids=None):
        """
        The ``acknowledgeMany`` action.
        
        :param obj_code_ids: objCodeIDs (type: ``map``)
        :return: ``string[]``
        """
        params = {}
        if obj_code_ids is not None: params['objCodeIDs'] = obj_code_ids
        data = self.session.put(self.api_url()+'/acknowledgeMany', params)
        return data['result']

    def unacknowledge(self, obj_code=None, obj_id=None):
        """
        The ``unacknowledge`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/unacknowledge', params)
        

api.register(Acknowledgement)


class Announcement(Object):
    code = 'ANCMNT'
    actual_subject = Field('actualSubject')
    announcement_type = Field('announcementType')
    content = Field('content')
    customer_recipients = Field('customerRecipients')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    formatted_recipients = Field('formattedRecipients')
    has_attachments = Field('hasAttachments')
    is_draft = Field('isDraft')
    last_sent_date = Field('lastSentDate')
    other_recipient_names = Field('otherRecipientNames')
    preview_user_id = Field('previewUserID')
    recipient_types = Field('recipientTypes')
    send_draft = Field('sendDraft')
    subject = Field('subject')
    summary = Field('summary')
    type = Field('type')
    entered_by = Reference('enteredBy')
    announcement_recipients = Collection('announcementRecipients')
    attachments = Collection('attachments')

    def file_handle(self, attachment_id=None):
        """
        The ``fileHandle`` action.
        
        :param attachment_id: attachmentID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if attachment_id is not None: params['attachmentID'] = attachment_id
        data = self.session.put(self.api_url()+'/fileHandle', params)
        return data['result']

    def zip_announcement_attachments(self, announcement_id=None):
        """
        The ``zipAnnouncementAttachments`` action.
        
        :param announcement_id: announcementID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if announcement_id is not None: params['announcementID'] = announcement_id
        data = self.session.put(self.api_url()+'/zipAnnouncementAttachments', params)
        return data['result']

api.register(Announcement)


class AnnouncementAttachment(Object):
    code = 'ANMATT'
    announcement_id = Field('announcementID')
    doc_size = Field('docSize')
    file_extension = Field('fileExtension')
    format_doc_size = Field('formatDocSize')
    name = Field('name')
    announcement = Reference('announcement')

    def forward_attachments(self, announcement_id=None, old_attachment_ids=None, new_attachments=None):
        """
        The ``forwardAttachments`` action.
        
        :param announcement_id: announcementID (type: ``string``)
        :param old_attachment_ids: oldAttachmentIDs (type: ``string[]``)
        :param new_attachments: newAttachments (type: ``map``)
        """
        params = {}
        if announcement_id is not None: params['announcementID'] = announcement_id
        if old_attachment_ids is not None: params['oldAttachmentIDs'] = old_attachment_ids
        if new_attachments is not None: params['newAttachments'] = new_attachments
        data = self.session.put(self.api_url()+'/forwardAttachments', params)
        

    def upload_attachments(self, announcement_id=None, attachments=None):
        """
        The ``uploadAttachments`` action.
        
        :param announcement_id: announcementID (type: ``string``)
        :param attachments: attachments (type: ``map``)
        """
        params = {}
        if announcement_id is not None: params['announcementID'] = announcement_id
        if attachments is not None: params['attachments'] = attachments
        data = self.session.put(self.api_url()+'/uploadAttachments', params)
        

api.register(AnnouncementAttachment)


class AnnouncementOptOut(Object):
    code = 'AMNTO'
    announcement_type = Field('announcementType')
    customer_id = Field('customerID')
    customer_name = Field('customerName')
    opt_out_date = Field('optOutDate')
    type = Field('type')
    user_first_name = Field('userFirstName')
    user_id = Field('userID')
    user_last_name = Field('userLastName')
    customer = Reference('customer')
    user = Reference('user')

    def announcement_opt_out(self, announcement_opt_out_types=None):
        """
        The ``announcementOptOut`` action.
        
        :param announcement_opt_out_types: announcementOptOutTypes (type: ``string[]``)
        """
        params = {}
        if announcement_opt_out_types is not None: params['announcementOptOutTypes'] = announcement_opt_out_types
        data = self.session.put(self.api_url()+'/announcementOptOut', params)
        

api.register(AnnouncementOptOut)


class AnnouncementRecipient(Object):
    code = 'ANCREC'
    announcement_id = Field('announcementID')
    company_id = Field('companyID')
    customer_id = Field('customerID')
    group_id = Field('groupID')
    recipient_id = Field('recipientID')
    recipient_obj_code = Field('recipientObjCode')
    role_id = Field('roleID')
    team_id = Field('teamID')
    user_id = Field('userID')
    announcement = Reference('announcement')
    company = Reference('company')
    customer = Reference('customer')
    group = Reference('group')
    role = Reference('role')
    team = Reference('team')
    user = Reference('user')

api.register(AnnouncementRecipient)


class AppBuild(Object):
    code = 'APPBLD'
    build_id = Field('buildID')
    build_number = Field('buildNumber')
    entry_date = Field('entryDate')

api.register(AppBuild)


class AppEvent(Object):
    code = 'APEVT'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    event_obj_code = Field('eventObjCode')
    event_type = Field('eventType')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    query_expression = Field('queryExpression')
    script_expression = Field('scriptExpression')
    app_global = Reference('appGlobal')
    customer = Reference('customer')

api.register(AppEvent)


class AppGlobal(Object):
    code = 'APGLOB'
    access_levels = Collection('accessLevels')
    access_scopes = Collection('accessScopes')
    app_events = Collection('appEvents')
    expense_types = Collection('expenseTypes')
    external_sections = Collection('externalSections')
    features_mapping = Collection('featuresMapping')
    hour_types = Collection('hourTypes')
    layout_templates = Collection('layoutTemplates')
    meta_records = Collection('metaRecords')
    portal_profiles = Collection('portalProfiles')
    portal_sections = Collection('portalSections')
    ui_filters = Collection('uiFilters')
    ui_group_bys = Collection('uiGroupBys')
    ui_views = Collection('uiViews')

api.register(AppGlobal)


class AppInfo(Object):
    code = 'APPINF'
    attask_version = Field('attaskVersion')
    build_number = Field('buildNumber')
    has_upgrade_error = Field('hasUpgradeError')
    last_update = Field('lastUpdate')
    upgrade_build = Field('upgradeBuild')
    upgrade_step = Field('upgradeStep')

api.register(AppInfo)


class Approval(Object):
    code = 'APPROVAL'
    bccompletion_state = Field('BCCompletionState')
    url = Field('URL')
    accessor_ids = Field('accessorIDs')
    actual_benefit = Field('actualBenefit')
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration = Field('actualDuration')
    actual_duration_expression = Field('actualDurationExpression')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_expense_cost = Field('actualExpenseCost')
    actual_hours_last_month = Field('actualHoursLastMonth')
    actual_hours_last_three_months = Field('actualHoursLastThreeMonths')
    actual_hours_this_month = Field('actualHoursThisMonth')
    actual_hours_two_months_ago = Field('actualHoursTwoMonthsAgo')
    actual_labor_cost = Field('actualLaborCost')
    actual_revenue = Field('actualRevenue')
    actual_risk_cost = Field('actualRiskCost')
    actual_start_date = Field('actualStartDate')
    actual_value = Field('actualValue')
    actual_work = Field('actualWork')
    actual_work_required = Field('actualWorkRequired')
    actual_work_required_expression = Field('actualWorkRequiredExpression')
    age_range_as_string = Field('ageRangeAsString')
    alignment = Field('alignment')
    alignment_score_card_id = Field('alignmentScoreCardID')
    all_approved_hours = Field('allApprovedHours')
    all_unapproved_hours = Field('allUnapprovedHours')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    assigned_to_id = Field('assignedToID')
    assignments_list_string = Field('assignmentsListString')
    audit_note = Field('auditNote')
    audit_types = Field('auditTypes')
    audit_user_ids = Field('auditUserIDs')
    auto_baseline_recur_on = Field('autoBaselineRecurOn')
    auto_baseline_recurrence_type = Field('autoBaselineRecurrenceType')
    auto_closure_date = Field('autoClosureDate')
    backlog_order = Field('backlogOrder')
    billed_revenue = Field('billedRevenue')
    billing_amount = Field('billingAmount')
    billing_record_id = Field('billingRecordID')
    budget = Field('budget')
    budget_status = Field('budgetStatus')
    budgeted_completion_date = Field('budgetedCompletionDate')
    budgeted_cost = Field('budgetedCost')
    budgeted_hours = Field('budgetedHours')
    budgeted_labor_cost = Field('budgetedLaborCost')
    budgeted_start_date = Field('budgetedStartDate')
    business_case_status_label = Field('businessCaseStatusLabel')
    can_start = Field('canStart')
    category_id = Field('categoryID')
    color = Field('color')
    commit_date = Field('commitDate')
    commit_date_range = Field('commitDateRange')
    company_id = Field('companyID')
    completion_pending_date = Field('completionPendingDate')
    completion_type = Field('completionType')
    condition = Field('condition')
    condition_type = Field('conditionType')
    constraint_date = Field('constraintDate')
    converted_op_task_entry_date = Field('convertedOpTaskEntryDate')
    converted_op_task_name = Field('convertedOpTaskName')
    converted_op_task_originator_id = Field('convertedOpTaskOriginatorID')
    cost_amount = Field('costAmount')
    cost_type = Field('costType')
    cpi = Field('cpi')
    csi = Field('csi')
    currency = Field('currency')
    current_approval_step_id = Field('currentApprovalStepID')
    current_status_duration = Field('currentStatusDuration')
    customer_id = Field('customerID')
    days_late = Field('daysLate')
    default_forbidden_contribute_actions = Field('defaultForbiddenContributeActions')
    default_forbidden_manage_actions = Field('defaultForbiddenManageActions')
    default_forbidden_view_actions = Field('defaultForbiddenViewActions')
    deliverable_score_card_id = Field('deliverableScoreCardID')
    deliverable_success_score = Field('deliverableSuccessScore')
    deliverable_success_score_ratio = Field('deliverableSuccessScoreRatio')
    description = Field('description')
    display_order = Field('displayOrder')
    display_queue_breadcrumb = Field('displayQueueBreadcrumb')
    due_date = Field('dueDate')
    duration = Field('duration')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    duration_type = Field('durationType')
    duration_unit = Field('durationUnit')
    eac = Field('eac')
    eac_calculation_method = Field('eacCalculationMethod')
    enable_auto_baselines = Field('enableAutoBaselines')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    estimate = Field('estimate')
    ext_ref_id = Field('extRefID')
    filter_hour_types = Field('filterHourTypes')
    finance_last_update_date = Field('financeLastUpdateDate')
    first_response = Field('firstResponse')
    fixed_cost = Field('fixedCost')
    fixed_end_date = Field('fixedEndDate')
    fixed_revenue = Field('fixedRevenue')
    fixed_start_date = Field('fixedStartDate')
    group_id = Field('groupID')
    handoff_date = Field('handoffDate')
    has_budget_conflict = Field('hasBudgetConflict')
    has_calc_error = Field('hasCalcError')
    has_completion_constraint = Field('hasCompletionConstraint')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_rate_override = Field('hasRateOverride')
    has_resolvables = Field('hasResolvables')
    has_start_constraint = Field('hasStartConstraint')
    has_timed_notifications = Field('hasTimedNotifications')
    has_timeline_exception = Field('hasTimelineException')
    hours_per_point = Field('hoursPerPoint')
    how_old = Field('howOld')
    indent = Field('indent')
    is_agile = Field('isAgile')
    is_complete = Field('isComplete')
    is_critical = Field('isCritical')
    is_duration_locked = Field('isDurationLocked')
    is_help_desk = Field('isHelpDesk')
    is_leveling_excluded = Field('isLevelingExcluded')
    is_project_dead = Field('isProjectDead')
    is_ready = Field('isReady')
    is_status_complete = Field('isStatusComplete')
    is_work_required_locked = Field('isWorkRequiredLocked')
    iteration_id = Field('iterationID')
    last_calc_date = Field('lastCalcDate')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_mode = Field('levelingMode')
    leveling_start_delay = Field('levelingStartDelay')
    leveling_start_delay_expression = Field('levelingStartDelayExpression')
    leveling_start_delay_minutes = Field('levelingStartDelayMinutes')
    lucid_migration_date = Field('lucidMigrationDate')
    master_task_id = Field('masterTaskID')
    milestone_id = Field('milestoneID')
    milestone_path_id = Field('milestonePathID')
    name = Field('name')
    next_auto_baseline_date = Field('nextAutoBaselineDate')
    number_of_children = Field('numberOfChildren')
    number_open_op_tasks = Field('numberOpenOpTasks')
    olv = Field('olv')
    op_task_type = Field('opTaskType')
    op_task_type_label = Field('opTaskTypeLabel')
    optimization_score = Field('optimizationScore')
    original_duration = Field('originalDuration')
    original_work_required = Field('originalWorkRequired')
    owner_id = Field('ownerID')
    owner_privileges = Field('ownerPrivileges')
    parent_id = Field('parentID')
    parent_lag = Field('parentLag')
    parent_lag_type = Field('parentLagType')
    pending_calculation = Field('pendingCalculation')
    pending_predecessors = Field('pendingPredecessors')
    pending_update_methods = Field('pendingUpdateMethods')
    percent_complete = Field('percentComplete')
    performance_index_method = Field('performanceIndexMethod')
    personal = Field('personal')
    planned_benefit = Field('plannedBenefit')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_duration = Field('plannedDuration')
    planned_duration_minutes = Field('plannedDurationMinutes')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_risk_cost = Field('plannedRiskCost')
    planned_start_date = Field('plannedStartDate')
    planned_value = Field('plannedValue')
    pop_account_id = Field('popAccountID')
    portfolio_id = Field('portfolioID')
    portfolio_priority = Field('portfolioPriority')
    predecessor_expression = Field('predecessorExpression')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    program_id = Field('programID')
    progress_status = Field('progressStatus')
    project_id = Field('projectID')
    projected_completion_date = Field('projectedCompletionDate')
    projected_duration_minutes = Field('projectedDurationMinutes')
    projected_start_date = Field('projectedStartDate')
    queue_def_id = Field('queueDefID')
    queue_topic_breadcrumb = Field('queueTopicBreadcrumb')
    queue_topic_id = Field('queueTopicID')
    recurrence_number = Field('recurrenceNumber')
    recurrence_rule_id = Field('recurrenceRuleID')
    reference_number = Field('referenceNumber')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_cost = Field('remainingCost')
    remaining_duration_minutes = Field('remainingDurationMinutes')
    remaining_revenue = Field('remainingRevenue')
    remaining_risk_cost = Field('remainingRiskCost')
    reserved_time_id = Field('reservedTimeID')
    resolution_time = Field('resolutionTime')
    resolve_op_task_id = Field('resolveOpTaskID')
    resolve_project_id = Field('resolveProjectID')
    resolve_task_id = Field('resolveTaskID')
    resolving_obj_code = Field('resolvingObjCode')
    resolving_obj_id = Field('resolvingObjID')
    resource_pool_id = Field('resourcePoolID')
    resource_scope = Field('resourceScope')
    revenue_type = Field('revenueType')
    risk = Field('risk')
    risk_performance_index = Field('riskPerformanceIndex')
    roi = Field('roi')
    role_id = Field('roleID')
    schedule_id = Field('scheduleID')
    schedule_mode = Field('scheduleMode')
    security_ancestors_disabled = Field('securityAncestorsDisabled')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    selected_on_portfolio_optimizer = Field('selectedOnPortfolioOptimizer')
    severity = Field('severity')
    show_commit_date = Field('showCommitDate')
    show_condition = Field('showCondition')
    show_status = Field('showStatus')
    slack_date = Field('slackDate')
    source_obj_code = Field('sourceObjCode')
    source_obj_id = Field('sourceObjID')
    source_task_id = Field('sourceTaskID')
    spi = Field('spi')
    sponsor_id = Field('sponsorID')
    status = Field('status')
    status_equates_with = Field('statusEquatesWith')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    summary_completion_type = Field('summaryCompletionType')
    task_constraint = Field('taskConstraint')
    task_number = Field('taskNumber')
    task_number_predecessor_string = Field('taskNumberPredecessorString')
    team_id = Field('teamID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    timeline_exception_info = Field('timelineExceptionInfo')
    total_hours = Field('totalHours')
    total_op_task_count = Field('totalOpTaskCount')
    total_task_count = Field('totalTaskCount')
    tracking_mode = Field('trackingMode')
    update_type = Field('updateType')
    url_ = Field('url')
    version = Field('version')
    wbs = Field('wbs')
    work = Field('work')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    work_unit = Field('workUnit')
    alignment_score_card = Reference('alignmentScoreCard')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    billing_record = Reference('billingRecord')
    category = Reference('category')
    company = Reference('company')
    converted_op_task_originator = Reference('convertedOpTaskOriginator')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    default_baseline = Reference('defaultBaseline')
    default_baseline_task = Reference('defaultBaselineTask')
    deliverable_score_card = Reference('deliverableScoreCard')
    entered_by = Reference('enteredBy')
    exchange_rate = Reference('exchangeRate')
    group = Reference('group')
    iteration = Reference('iteration')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    master_task = Reference('masterTask')
    milestone = Reference('milestone')
    milestone_path = Reference('milestonePath')
    owner = Reference('owner')
    parent = Reference('parent')
    pop_account = Reference('popAccount')
    portfolio = Reference('portfolio')
    primary_assignment = Reference('primaryAssignment')
    program = Reference('program')
    project = Reference('project')
    queue_def = Reference('queueDef')
    queue_topic = Reference('queueTopic')
    recurrence_rule = Reference('recurrenceRule')
    rejection_issue = Reference('rejectionIssue')
    reserved_time = Reference('reservedTime')
    resolve_op_task = Reference('resolveOpTask')
    resolve_project = Reference('resolveProject')
    resolve_task = Reference('resolveTask')
    resource_pool = Reference('resourcePool')
    role = Reference('role')
    schedule = Reference('schedule')
    sharing_settings = Reference('sharingSettings')
    source_task = Reference('sourceTask')
    sponsor = Reference('sponsor')
    submitted_by = Reference('submittedBy')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    template = Reference('template')
    template_task = Reference('templateTask')
    work_item = Reference('workItem')
    access_rules = Collection('accessRules')
    alignment_values = Collection('alignmentValues')
    all_hours = Collection('allHours')
    all_priorities = Collection('allPriorities')
    all_severities = Collection('allSeverities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    assignments = Collection('assignments')
    awaiting_approvals = Collection('awaitingApprovals')
    baselines = Collection('baselines')
    billing_records = Collection('billingRecords')
    children = Collection('children')
    deliverable_values = Collection('deliverableValues')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    done_statuses = Collection('doneStatuses')
    exchange_rates = Collection('exchangeRates')
    expenses = Collection('expenses')
    hour_types = Collection('hourTypes')
    hours = Collection('hours')
    notification_records = Collection('notificationRecords')
    object_categories = Collection('objectCategories')
    op_tasks = Collection('opTasks')
    open_op_tasks = Collection('openOpTasks')
    parameter_values = Collection('parameterValues')
    predecessors = Collection('predecessors')
    project_user_roles = Collection('projectUserRoles')
    project_users = Collection('projectUsers')
    rates = Collection('rates')
    resolvables = Collection('resolvables')
    resource_allocations = Collection('resourceAllocations')
    risks = Collection('risks')
    roles = Collection('roles')
    routing_rules = Collection('routingRules')
    security_ancestors = Collection('securityAncestors')
    successors = Collection('successors')
    tasks = Collection('tasks')
    updates = Collection('updates')

    def is_in_my_approvals(self, object_type=None, object_id=None):
        """
        The ``isInMyApprovals`` action.
        
        :param object_type: objectType (type: ``string``)
        :param object_id: objectID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if object_type is not None: params['objectType'] = object_type
        if object_id is not None: params['objectID'] = object_id
        data = self.session.put(self.api_url()+'/isInMyApprovals', params)
        return data['result']

    def is_in_my_submitted_approvals(self, object_type=None, object_id=None):
        """
        The ``isInMySubmittedApprovals`` action.
        
        :param object_type: objectType (type: ``string``)
        :param object_id: objectID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if object_type is not None: params['objectType'] = object_type
        if object_id is not None: params['objectID'] = object_id
        data = self.session.put(self.api_url()+'/isInMySubmittedApprovals', params)
        return data['result']

api.register(Approval)


class ApprovalPath(Object):
    code = 'ARVPTH'
    approval_process_id = Field('approvalProcessID')
    customer_id = Field('customerID')
    duration_minutes = Field('durationMinutes')
    duration_unit = Field('durationUnit')
    rejected_status = Field('rejectedStatus')
    rejected_status_label = Field('rejectedStatusLabel')
    should_create_issue = Field('shouldCreateIssue')
    target_status = Field('targetStatus')
    target_status_label = Field('targetStatusLabel')
    approval_process = Reference('approvalProcess')
    customer = Reference('customer')
    approval_steps = Collection('approvalSteps')

api.register(ApprovalPath)


class ApprovalProcess(Object):
    code = 'ARVPRC'
    accessor_ids = Field('accessorIDs')
    approval_obj_code = Field('approvalObjCode')
    approval_statuses = Field('approvalStatuses')
    customer_id = Field('customerID')
    description = Field('description')
    duration_minutes = Field('durationMinutes')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    is_private = Field('isPrivate')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    approval_paths = Collection('approvalPaths')

api.register(ApprovalProcess)


class ApprovalProcessAttachable(Object):
    code = 'APRPROCATCH'
    allowed_actions = Field('allowedActions')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    category_id = Field('categoryID')
    current_approval_step_id = Field('currentApprovalStepID')
    force_edit = Field('forceEdit')
    previous_status = Field('previousStatus')
    rejection_issue_id = Field('rejectionIssueID')
    submitted_by_id = Field('submittedByID')
    approval_process = Reference('approvalProcess')
    category = Reference('category')
    current_approval_step = Reference('currentApprovalStep')
    rejection_issue = Reference('rejectionIssue')
    submitted_by = Reference('submittedBy')
    approver_statuses = Collection('approverStatuses')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')

api.register(ApprovalProcessAttachable)


class ApprovalStep(Object):
    code = 'ARVSTP'
    approval_path_id = Field('approvalPathID')
    approval_type = Field('approvalType')
    customer_id = Field('customerID')
    name = Field('name')
    sequence_number = Field('sequenceNumber')
    approval_path = Reference('approvalPath')
    customer = Reference('customer')
    step_approvers = Collection('stepApprovers')

api.register(ApprovalStep)


class ApproverStatus(Object):
    code = 'ARVSTS'
    approvable_obj_code = Field('approvableObjCode')
    approvable_obj_id = Field('approvableObjID')
    approval_step_id = Field('approvalStepID')
    approved_by_id = Field('approvedByID')
    customer_id = Field('customerID')
    delegate_user_id = Field('delegateUserID')
    is_overridden = Field('isOverridden')
    op_task_id = Field('opTaskID')
    overridden_user_id = Field('overriddenUserID')
    project_id = Field('projectID')
    status = Field('status')
    step_approver_id = Field('stepApproverID')
    task_id = Field('taskID')
    wildcard_user_id = Field('wildcardUserID')
    approval_step = Reference('approvalStep')
    approved_by = Reference('approvedBy')
    customer = Reference('customer')
    delegate_user = Reference('delegateUser')
    op_task = Reference('opTask')
    overridden_user = Reference('overriddenUser')
    project = Reference('project')
    step_approver = Reference('stepApprover')
    task = Reference('task')
    wildcard_user = Reference('wildcardUser')

api.register(ApproverStatus)


class Assignment(Object):
    code = 'ASSGN'
    accessor_ids = Field('accessorIDs')
    actual_work_completed = Field('actualWorkCompleted')
    actual_work_per_day_start_date = Field('actualWorkPerDayStartDate')
    assigned_by_id = Field('assignedByID')
    assigned_to_id = Field('assignedToID')
    assignment_percent = Field('assignmentPercent')
    avg_work_per_day = Field('avgWorkPerDay')
    customer_id = Field('customerID')
    feedback_status = Field('feedbackStatus')
    is_primary = Field('isPrimary')
    is_team_assignment = Field('isTeamAssignment')
    olv = Field('olv')
    op_task_id = Field('opTaskID')
    planned_user_allocation_percentage = Field('plannedUserAllocationPercentage')
    project_id = Field('projectID')
    projected_avg_work_per_day = Field('projectedAvgWorkPerDay')
    projected_user_allocation_percentage = Field('projectedUserAllocationPercentage')
    role_id = Field('roleID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    status = Field('status')
    task_id = Field('taskID')
    team_id = Field('teamID')
    work = Field('work')
    work_required = Field('workRequired')
    work_unit = Field('workUnit')
    assigned_by = Reference('assignedBy')
    assigned_to = Reference('assignedTo')
    customer = Reference('customer')
    op_task = Reference('opTask')
    project = Reference('project')
    role = Reference('role')
    task = Reference('task')
    team = Reference('team')
    work_item = Reference('workItem')

api.register(Assignment)


class AuditLoginAsSession(Object):
    code = 'AUDS'
    action_count = Field('actionCount')
    customer_id = Field('customerID')
    end_date = Field('endDate')
    note_count = Field('noteCount')
    session_id = Field('sessionID')
    start_date = Field('startDate')
    target_user_display = Field('targetUserDisplay')
    target_user_id = Field('targetUserID')
    user_display = Field('userDisplay')
    user_id = Field('userID')
    customer = Reference('customer')
    target_user = Reference('targetUser')
    user = Reference('user')
    journal_entries = Collection('journalEntries')
    notes = Collection('notes')

    def all_accessed_users(self):
        """
        The ``allAccessedUsers`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/allAccessedUsers', params)
        return data['result']

    def all_admins(self):
        """
        The ``allAdmins`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/allAdmins', params)
        return data['result']

    def audit_session(self, user_id=None, target_user_id=None):
        """
        The ``auditSession`` action.
        
        :param user_id: userID (type: ``string``)
        :param target_user_id: targetUserID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if target_user_id is not None: params['targetUserID'] = target_user_id
        data = self.session.put(self.api_url()+'/auditSession', params)
        return data['result']

    def end_audit(self, session_id=None):
        """
        The ``endAudit`` action.
        
        :param session_id: sessionID (type: ``string``)
        """
        params = {}
        if session_id is not None: params['sessionID'] = session_id
        data = self.session.put(self.api_url()+'/endAudit', params)
        

    def get_accessed_users(self, user_id=None):
        """
        The ``getAccessedUsers`` action.
        
        :param user_id: userID (type: ``string``)
        :return: ``map``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/getAccessedUsers', params)
        return data['result']

    def who_accessed_user(self, user_id=None):
        """
        The ``whoAccessedUser`` action.
        
        :param user_id: userID (type: ``string``)
        :return: ``map``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/whoAccessedUser', params)
        return data['result']

api.register(AuditLoginAsSession)


class Authentication(Object):
    code = 'AUTH'
    obj_code = Field('objCode')

    def create_public_session(self):
        """
        The ``createPublicSession`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/createPublicSession', params)
        return data['result']

    def create_schema(self):
        """
        The ``createSchema`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/createSchema', params)
        

    def create_session(self):
        """
        The ``createSession`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/createSession', params)
        return data['result']

    def get_days_to_expiration_for_user(self):
        """
        The ``getDaysToExpirationForUser`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDaysToExpirationForUser', params)
        return data['result']

    def get_password_complexity_by_token(self, token=None):
        """
        The ``getPasswordComplexityByToken`` action.
        
        :param token: token (type: ``string``)
        :return: ``string``
        """
        params = {}
        if token is not None: params['token'] = token
        data = self.session.put(self.api_url()+'/getPasswordComplexityByToken', params)
        return data['result']

    def get_password_complexity_by_username(self, username=None):
        """
        The ``getPasswordComplexityByUsername`` action.
        
        :param username: username (type: ``string``)
        :return: ``string``
        """
        params = {}
        if username is not None: params['username'] = username
        data = self.session.put(self.api_url()+'/getPasswordComplexityByUsername', params)
        return data['result']

    def get_ssooption_by_domain(self, domain=None):
        """
        The ``getSSOOptionByDomain`` action.
        
        :param domain: domain (type: ``string``)
        :return: ``map``
        """
        params = {}
        if domain is not None: params['domain'] = domain
        data = self.session.put(self.api_url()+'/getSSOOptionByDomain', params)
        return data['result']

    def get_upgrades_info(self):
        """
        The ``getUpgradesInfo`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getUpgradesInfo', params)
        return data['result']

    def login_with_user_name(self, session_id=None, username=None):
        """
        The ``loginWithUserName`` action.
        
        :param session_id: sessionID (type: ``string``)
        :param username: username (type: ``string``)
        :return: ``map``
        """
        params = {}
        if session_id is not None: params['sessionID'] = session_id
        if username is not None: params['username'] = username
        data = self.session.put(self.api_url()+'/loginWithUserName', params)
        return data['result']

    def login_with_user_name_and_password(self, username=None, password=None):
        """
        The ``loginWithUserNameAndPassword`` action.
        
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :return: ``map``
        """
        params = {}
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        data = self.session.put(self.api_url()+'/loginWithUserNameAndPassword', params)
        return data['result']

    def logout(self, sso_user=None, is_mobile=None):
        """
        The ``logout`` action.
        
        :param sso_user: ssoUser (type: ``boolean``)
        :param is_mobile: isMobile (type: ``boolean``)
        """
        params = {}
        if sso_user is not None: params['ssoUser'] = sso_user
        if is_mobile is not None: params['isMobile'] = is_mobile
        data = self.session.put(self.api_url()+'/logout', params)
        

    def perform_upgrade(self):
        """
        The ``performUpgrade`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/performUpgrade', params)
        

    def reset_password(self, user_name=None, old_password=None, new_password=None):
        """
        The ``resetPassword`` action.
        
        :param user_name: userName (type: ``string``)
        :param old_password: oldPassword (type: ``string``)
        :param new_password: newPassword (type: ``string``)
        """
        params = {}
        if user_name is not None: params['userName'] = user_name
        if old_password is not None: params['oldPassword'] = old_password
        if new_password is not None: params['newPassword'] = new_password
        data = self.session.put(self.api_url()+'/resetPassword', params)
        

    def reset_password_by_token(self, token=None, new_password=None):
        """
        The ``resetPasswordByToken`` action.
        
        :param token: token (type: ``string``)
        :param new_password: newPassword (type: ``string``)
        :return: ``string``
        """
        params = {}
        if token is not None: params['token'] = token
        if new_password is not None: params['newPassword'] = new_password
        data = self.session.put(self.api_url()+'/resetPasswordByToken', params)
        return data['result']

    def upgrade_progress(self):
        """
        The ``upgradeProgress`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/upgradeProgress', params)
        return data['result']

api.register(Authentication)


class Avatar(Object):
    code = 'AVATAR'
    allowed_actions = Field('allowedActions')
    avatar_date = Field('avatarDate')
    avatar_download_url = Field('avatarDownloadURL')
    avatar_size = Field('avatarSize')
    avatar_x = Field('avatarX')
    avatar_y = Field('avatarY')
    handle = Field('handle')

    def crop_unsaved_avatar_file(self, handle=None, width=None, height=None, avatar_x=None, avatar_y=None):
        """
        The ``cropUnsavedAvatarFile`` action.
        
        :param handle: handle (type: ``string``)
        :param width: width (type: ``int``)
        :param height: height (type: ``int``)
        :param avatar_x: avatarX (type: ``int``)
        :param avatar_y: avatarY (type: ``int``)
        :return: ``string``
        """
        params = {}
        if handle is not None: params['handle'] = handle
        if width is not None: params['width'] = width
        if height is not None: params['height'] = height
        if avatar_x is not None: params['avatarX'] = avatar_x
        if avatar_y is not None: params['avatarY'] = avatar_y
        data = self.session.put(self.api_url()+'/cropUnsavedAvatarFile', params)
        return data['result']

    def get_avatar_data(self, obj_code=None, obj_id=None, size=None):
        """
        The ``getAvatarData`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :param size: size (type: ``string``)
        :return: ``string``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        if size is not None: params['size'] = size
        data = self.session.put(self.api_url()+'/getAvatarData', params)
        return data['result']

    def get_avatar_download_url(self, obj_code=None, obj_id=None, size=None, no_grayscale=None, public_token=None):
        """
        The ``getAvatarDownloadURL`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :param size: size (type: ``string``)
        :param no_grayscale: noGrayscale (type: ``boolean``)
        :param public_token: publicToken (type: ``string``)
        :return: ``string``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        if size is not None: params['size'] = size
        if no_grayscale is not None: params['noGrayscale'] = no_grayscale
        if public_token is not None: params['publicToken'] = public_token
        data = self.session.put(self.api_url()+'/getAvatarDownloadURL', params)
        return data['result']

    def get_avatar_file(self, obj_code=None, obj_id=None, size=None, no_grayscale=None):
        """
        The ``getAvatarFile`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :param size: size (type: ``string``)
        :param no_grayscale: noGrayscale (type: ``boolean``)
        :return: ``string``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        if size is not None: params['size'] = size
        if no_grayscale is not None: params['noGrayscale'] = no_grayscale
        data = self.session.put(self.api_url()+'/getAvatarFile', params)
        return data['result']

    def resize_unsaved_avatar_file(self, handle=None, width=None, height=None):
        """
        The ``resizeUnsavedAvatarFile`` action.
        
        :param handle: handle (type: ``string``)
        :param width: width (type: ``int``)
        :param height: height (type: ``int``)
        """
        params = {}
        if handle is not None: params['handle'] = handle
        if width is not None: params['width'] = width
        if height is not None: params['height'] = height
        data = self.session.put(self.api_url()+'/resizeUnsavedAvatarFile', params)
        

api.register(Avatar)


class AwaitingApproval(Object):
    code = 'AWAPVL'
    access_request_id = Field('accessRequestID')
    approvable_id = Field('approvableID')
    approver_id = Field('approverID')
    customer_id = Field('customerID')
    document_id = Field('documentID')
    entry_date = Field('entryDate')
    op_task_id = Field('opTaskID')
    project_id = Field('projectID')
    role_id = Field('roleID')
    submitted_by_id = Field('submittedByID')
    task_id = Field('taskID')
    team_id = Field('teamID')
    timesheet_id = Field('timesheetID')
    user_id = Field('userID')
    access_request = Reference('accessRequest')
    customer = Reference('customer')
    document = Reference('document')
    op_task = Reference('opTask')
    project = Reference('project')
    role = Reference('role')
    submitted_by = Reference('submittedBy')
    task = Reference('task')
    team = Reference('team')
    timesheet = Reference('timesheet')
    user = Reference('user')

    def get_my_awaiting_approvals_count(self):
        """
        The ``getMyAwaitingApprovalsCount`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getMyAwaitingApprovalsCount', params)
        return data['result']

    def get_my_awaiting_approvals_filtered_count(self, object_type=None):
        """
        The ``getMyAwaitingApprovalsFilteredCount`` action.
        
        :param object_type: objectType (type: ``string``)
        :return: ``java.lang.Integer``
        """
        params = {}
        if object_type is not None: params['objectType'] = object_type
        data = self.session.put(self.api_url()+'/getMyAwaitingApprovalsFilteredCount', params)
        return data['result']

    def get_my_submitted_awaiting_approvals_count(self):
        """
        The ``getMySubmittedAwaitingApprovalsCount`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getMySubmittedAwaitingApprovalsCount', params)
        return data['result']

api.register(AwaitingApproval)


class BackgroundJob(Object):
    code = 'BKGJOB'
    access_count = Field('accessCount')
    cache_key = Field('cacheKey')
    changed_objects = Field('changedObjects')
    customer_id = Field('customerID')
    end_date = Field('endDate')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    error_message = Field('errorMessage')
    expiration_date = Field('expirationDate')
    handler_class_name = Field('handlerClassName')
    max_progress = Field('maxProgress')
    percent_complete = Field('percentComplete')
    progress = Field('progress')
    progress_text = Field('progressText')
    start_date = Field('startDate')
    status = Field('status')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')

    def can_enqueue_export(self):
        """
        The ``canEnqueueExport`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/canEnqueueExport', params)
        return data['result']

    def file_for_completed_job(self, increase_access_count=None):
        """
        The ``fileForCompletedJob`` action.
        
        :param increase_access_count: increaseAccessCount (type: ``boolean``)
        :return: ``string``
        """
        params = {}
        if increase_access_count is not None: params['increaseAccessCount'] = increase_access_count
        data = self.session.put(self.api_url()+'/fileForCompletedJob', params)
        return data['result']

    def migrate_journal_field_wild_card(self):
        """
        The ``migrateJournalFieldWildCard`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/migrateJournalFieldWildCard', params)
        return data['result']

    def migrate_ppmto_anaconda(self):
        """
        The ``migratePPMToAnaconda`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/migratePPMToAnaconda', params)
        return data['result']

    def running_jobs_count(self, handler_class_name=None):
        """
        The ``runningJobsCount`` action.
        
        :param handler_class_name: handlerClassName (type: ``string``)
        :return: ``java.lang.Integer``
        """
        params = {}
        if handler_class_name is not None: params['handlerClassName'] = handler_class_name
        data = self.session.put(self.api_url()+'/runningJobsCount', params)
        return data['result']

    def start_kick_start_download(self, export_object_map=None, objcodes=None, exclude_demo_data=None, new_ooxmlformat=None, populate_existing_data=None):
        """
        The ``startKickStartDownload`` action.
        
        :param export_object_map: exportObjectMap (type: ``map``)
        :param objcodes: objcodes (type: ``string[]``)
        :param exclude_demo_data: excludeDemoData (type: ``boolean``)
        :param new_ooxmlformat: newOOXMLFormat (type: ``boolean``)
        :param populate_existing_data: populateExistingData (type: ``boolean``)
        :return: ``string``
        """
        params = {}
        if export_object_map is not None: params['exportObjectMap'] = export_object_map
        if objcodes is not None: params['objcodes'] = objcodes
        if exclude_demo_data is not None: params['excludeDemoData'] = exclude_demo_data
        if new_ooxmlformat is not None: params['newOOXMLFormat'] = new_ooxmlformat
        if populate_existing_data is not None: params['populateExistingData'] = populate_existing_data
        data = self.session.put(self.api_url()+'/startKickStartDownload', params)
        return data['result']

api.register(BackgroundJob)


class Baseline(Object):
    code = 'BLIN'
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_start_date = Field('actualStartDate')
    actual_work_required = Field('actualWorkRequired')
    auto_generated = Field('autoGenerated')
    budget = Field('budget')
    condition = Field('condition')
    cpi = Field('cpi')
    csi = Field('csi')
    customer_id = Field('customerID')
    duration_minutes = Field('durationMinutes')
    eac = Field('eac')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    is_default = Field('isDefault')
    name = Field('name')
    percent_complete = Field('percentComplete')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_start_date = Field('plannedStartDate')
    progress_status = Field('progressStatus')
    project_id = Field('projectID')
    projected_completion_date = Field('projectedCompletionDate')
    projected_start_date = Field('projectedStartDate')
    spi = Field('spi')
    work_required = Field('workRequired')
    customer = Reference('customer')
    project = Reference('project')
    baseline_tasks = Collection('baselineTasks')

api.register(Baseline)


class BaselineTask(Object):
    code = 'BSTSK'
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_start_date = Field('actualStartDate')
    actual_work_required = Field('actualWorkRequired')
    baseline_id = Field('baselineID')
    cpi = Field('cpi')
    csi = Field('csi')
    customer_id = Field('customerID')
    duration_minutes = Field('durationMinutes')
    duration_unit = Field('durationUnit')
    eac = Field('eac')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    is_default = Field('isDefault')
    name = Field('name')
    percent_complete = Field('percentComplete')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_start_date = Field('plannedStartDate')
    progress_status = Field('progressStatus')
    projected_completion_date = Field('projectedCompletionDate')
    projected_start_date = Field('projectedStartDate')
    spi = Field('spi')
    task_id = Field('taskID')
    work_required = Field('workRequired')
    baseline = Reference('baseline')
    customer = Reference('customer')
    task = Reference('task')

api.register(BaselineTask)


class BillingRecord(Object):
    code = 'BILL'
    accessor_ids = Field('accessorIDs')
    amount = Field('amount')
    billing_date = Field('billingDate')
    customer_id = Field('customerID')
    description = Field('description')
    display_name = Field('displayName')
    ext_ref_id = Field('extRefID')
    invoice_id = Field('invoiceID')
    other_amount = Field('otherAmount')
    po_number = Field('poNumber')
    project_id = Field('projectID')
    status = Field('status')
    customer = Reference('customer')
    project = Reference('project')
    billable_tasks = Collection('billableTasks')
    expenses = Collection('expenses')
    hours = Collection('hours')

api.register(BillingRecord)


class Branding(Object):
    code = 'BRND'
    customer_id = Field('customerID')
    details = Field('details')
    last_update_date = Field('lastUpdateDate')
    customer = Reference('customer')

api.register(Branding)


class BurndownEvent(Object):
    code = 'BDNEVT'
    apply_date = Field('applyDate')
    burndown_obj_code = Field('burndownObjCode')
    burndown_obj_id = Field('burndownObjID')
    customer_id = Field('customerID')
    delta_points_complete = Field('deltaPointsComplete')
    delta_total_items = Field('deltaTotalItems')
    delta_total_points = Field('deltaTotalPoints')
    entry_date = Field('entryDate')
    event_obj_code = Field('eventObjCode')
    event_obj_id = Field('eventObjID')
    is_complete = Field('isComplete')
    customer = Reference('customer')

api.register(BurndownEvent)


class CalendarEvent(Object):
    code = 'CALEVT'
    calendar_section_id = Field('calendarSectionID')
    color = Field('color')
    customer_id = Field('customerID')
    description = Field('description')
    end_date = Field('endDate')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    start_date = Field('startDate')
    calendar_section = Reference('calendarSection')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')

api.register(CalendarEvent)


class CalendarFeedEntry(Object):
    code = 'CALITM'
    allowed_actions = Field('allowedActions')
    assigned_to_id = Field('assignedToID')
    assigned_to_name = Field('assignedToName')
    assigned_to_title = Field('assignedToTitle')
    calendar_event_id = Field('calendarEventID')
    calendar_section_ids = Field('calendarSectionIDs')
    color = Field('color')
    due_date = Field('dueDate')
    end_date = Field('endDate')
    obj_code = Field('objCode')
    op_task_id = Field('opTaskID')
    percent_complete = Field('percentComplete')
    project_display_name = Field('projectDisplayName')
    project_id = Field('projectID')
    ref_name = Field('refName')
    ref_obj_code = Field('refObjCode')
    ref_obj_id = Field('refObjID')
    start_date = Field('startDate')
    status = Field('status')
    task_id = Field('taskID')
    calendar_event = Reference('calendarEvent')
    op_task = Reference('opTask')
    project = Reference('project')
    task = Reference('task')

api.register(CalendarFeedEntry)


class CalendarInfo(Object):
    code = 'CALEND'
    accessor_ids = Field('accessorIDs')
    customer_id = Field('customerID')
    is_public = Field('isPublic')
    name = Field('name')
    public_token = Field('publicToken')
    run_as_user_id = Field('runAsUserID')
    security_ancestors_disabled = Field('securityAncestorsDisabled')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    user_id = Field('userID')
    customer = Reference('customer')
    run_as_user = Reference('runAsUser')
    user = Reference('user')
    access_rules = Collection('accessRules')
    calendar_sections = Collection('calendarSections')
    security_ancestors = Collection('securityAncestors')

    def create_first_calendar(self):
        """
        The ``createFirstCalendar`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/createFirstCalendar', params)
        return data['result']

    def create_project_section(self, project_id=None, color=None):
        """
        The ``createProjectSection`` action.
        
        :param project_id: projectID (type: ``string``)
        :param color: color (type: ``string``)
        :return: ``string``
        """
        params = {}
        if project_id is not None: params['projectID'] = project_id
        if color is not None: params['color'] = color
        data = self.session.put(self.api_url()+'/createProjectSection', params)
        return data['result']

api.register(CalendarInfo)


class CalendarPortalSection(Object):
    code = 'CALPTL'
    calendar_info_id = Field('calendarInfoID')
    customer_id = Field('customerID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    calendar_info = Reference('calendarInfo')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')

api.register(CalendarPortalSection)


class CalendarSection(Object):
    code = 'CALSEC'
    cal_events = Field('calEvents')
    calendar_id = Field('calendarID')
    color = Field('color')
    customer_id = Field('customerID')
    duration = Field('duration')
    milestone = Field('milestone')
    name = Field('name')
    planned_date = Field('plannedDate')
    start_date = Field('startDate')
    calendar = Reference('calendar')
    customer = Reference('customer')
    calendar_events = Collection('calendarEvents')
    callable_expressions = Collection('callableExpressions')
    filters = Collection('filters')

    def get_concatenated_expression_form(self, expression=None):
        """
        The ``getConcatenatedExpressionForm`` action.
        
        :param expression: expression (type: ``string``)
        :return: ``string``
        """
        params = {}
        if expression is not None: params['expression'] = expression
        data = self.session.put(self.api_url()+'/getConcatenatedExpressionForm', params)
        return data['result']

    def get_pretty_expression_form(self, expression=None):
        """
        The ``getPrettyExpressionForm`` action.
        
        :param expression: expression (type: ``string``)
        :return: ``string``
        """
        params = {}
        if expression is not None: params['expression'] = expression
        data = self.session.put(self.api_url()+'/getPrettyExpressionForm', params)
        return data['result']

api.register(CalendarSection)


class CallableExpression(Object):
    code = 'CALEXP'
    customer_id = Field('customerID')
    expression = Field('expression')
    ui_obj_code = Field('uiObjCode')
    customer = Reference('customer')

    def validate_callable_expression(self, custom_expression=None):
        """
        The ``validateCallableExpression`` action.
        
        :param custom_expression: customExpression (type: ``string``)
        """
        params = {}
        if custom_expression is not None: params['customExpression'] = custom_expression
        data = self.session.put(self.api_url()+'/validateCallableExpression', params)
        

api.register(CallableExpression)


class Category(Object):
    code = 'CTGY'
    accessor_ids = Field('accessorIDs')
    cat_obj_code = Field('catObjCode')
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    ext_ref_id = Field('extRefID')
    group_id = Field('groupID')
    has_calculated_fields = Field('hasCalculatedFields')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    group = Reference('group')
    last_updated_by = Reference('lastUpdatedBy')
    access_rules = Collection('accessRules')
    category_access_rules = Collection('categoryAccessRules')
    category_cascade_rules = Collection('categoryCascadeRules')
    category_parameters = Collection('categoryParameters')
    other_groups = Collection('otherGroups')

    def assign_categories(self, obj_id=None, obj_code=None, category_ids=None):
        """
        The ``assignCategories`` action.
        
        :param obj_id: objID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param category_ids: categoryIDs (type: ``string[]``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if obj_code is not None: params['objCode'] = obj_code
        if category_ids is not None: params['categoryIDs'] = category_ids
        data = self.session.put(self.api_url()+'/assignCategories', params)
        

    def assign_category(self, obj_id=None, obj_code=None, category_id=None):
        """
        The ``assignCategory`` action.
        
        :param obj_id: objID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param category_id: categoryID (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if obj_code is not None: params['objCode'] = obj_code
        if category_id is not None: params['categoryID'] = category_id
        data = self.session.put(self.api_url()+'/assignCategory', params)
        

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def get_expression_types(self):
        """
        The ``getExpressionTypes`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getExpressionTypes', params)
        return data['result']

    def get_filtered_categories(self, obj_code=None, object_id=None, object_map=None):
        """
        The ``getFilteredCategories`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param object_id: objectID (type: ``string``)
        :param object_map: objectMap (type: ``map``)
        :return: ``string[]``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if object_id is not None: params['objectID'] = object_id
        if object_map is not None: params['objectMap'] = object_map
        data = self.session.put(self.api_url()+'/getFilteredCategories', params)
        return data['result']

    def get_formula_calculated_expression(self, custom_expression=None):
        """
        The ``getFormulaCalculatedExpression`` action.
        
        :param custom_expression: customExpression (type: ``string``)
        :return: ``string``
        """
        params = {}
        if custom_expression is not None: params['customExpression'] = custom_expression
        data = self.session.put(self.api_url()+'/getFormulaCalculatedExpression', params)
        return data['result']

    def get_friendly_calculated_expression(self, custom_expression=None):
        """
        The ``getFriendlyCalculatedExpression`` action.
        
        :param custom_expression: customExpression (type: ``string``)
        :return: ``string``
        """
        params = {}
        if custom_expression is not None: params['customExpression'] = custom_expression
        data = self.session.put(self.api_url()+'/getFriendlyCalculatedExpression', params)
        return data['result']

    def reorder_categories(self, obj_id=None, obj_code=None, category_ids=None):
        """
        The ``reorderCategories`` action.
        
        :param obj_id: objID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param category_ids: categoryIDs (type: ``string[]``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if obj_code is not None: params['objCode'] = obj_code
        if category_ids is not None: params['categoryIDs'] = category_ids
        data = self.session.put(self.api_url()+'/reorderCategories', params)
        

    def unassign_categories(self, obj_id=None, obj_code=None, category_ids=None):
        """
        The ``unassignCategories`` action.
        
        :param obj_id: objID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param category_ids: categoryIDs (type: ``string[]``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if obj_code is not None: params['objCode'] = obj_code
        if category_ids is not None: params['categoryIDs'] = category_ids
        data = self.session.put(self.api_url()+'/unassignCategories', params)
        

    def unassign_category(self, obj_id=None, obj_code=None, category_id=None):
        """
        The ``unassignCategory`` action.
        
        :param obj_id: objID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param category_id: categoryID (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if obj_code is not None: params['objCode'] = obj_code
        if category_id is not None: params['categoryID'] = category_id
        data = self.session.put(self.api_url()+'/unassignCategory', params)
        

    def update_calculated_parameter_values(self, category_id=None, parameter_ids=None, should_auto_commit=None):
        """
        The ``updateCalculatedParameterValues`` action.
        
        :param category_id: categoryID (type: ``string``)
        :param parameter_ids: parameterIDs (type: ``string[]``)
        :param should_auto_commit: shouldAutoCommit (type: ``boolean``)
        """
        params = {}
        if category_id is not None: params['categoryID'] = category_id
        if parameter_ids is not None: params['parameterIDs'] = parameter_ids
        if should_auto_commit is not None: params['shouldAutoCommit'] = should_auto_commit
        data = self.session.put(self.api_url()+'/updateCalculatedParameterValues', params)
        

    def validate_custom_expression(self, cat_obj_code=None, custom_expression=None):
        """
        The ``validateCustomExpression`` action.
        
        :param cat_obj_code: catObjCode (type: ``string``)
        :param custom_expression: customExpression (type: ``string``)
        """
        params = {}
        if cat_obj_code is not None: params['catObjCode'] = cat_obj_code
        if custom_expression is not None: params['customExpression'] = custom_expression
        data = self.session.put(self.api_url()+'/validateCustomExpression', params)
        

api.register(Category)


class CategoryAccessRule(Object):
    code = 'CATACR'
    accessor_id = Field('accessorID')
    accessor_obj_code = Field('accessorObjCode')
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    category = Reference('category')
    customer = Reference('customer')

api.register(CategoryAccessRule)


class CategoryCascadeRule(Object):
    code = 'CTCSRL'
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    next_parameter_group_id = Field('nextParameterGroupID')
    next_parameter_id = Field('nextParameterID')
    otherwise_parameter_id = Field('otherwiseParameterID')
    rule_type = Field('ruleType')
    to_end_of_form = Field('toEndOfForm')
    category = Reference('category')
    customer = Reference('customer')
    next_parameter = Reference('nextParameter')
    next_parameter_group = Reference('nextParameterGroup')
    otherwise_parameter = Reference('otherwiseParameter')
    category_cascade_rule_matches = Collection('categoryCascadeRuleMatches')

api.register(CategoryCascadeRule)


class CategoryCascadeRuleMatch(Object):
    code = 'CTCSRM'
    category_cascade_rule_id = Field('categoryCascadeRuleID')
    customer_id = Field('customerID')
    match_type = Field('matchType')
    parameter_id = Field('parameterID')
    value = Field('value')
    category_cascade_rule = Reference('categoryCascadeRule')
    customer = Reference('customer')
    parameter = Reference('parameter')

api.register(CategoryCascadeRuleMatch)


class CategoryParameter(Object):
    code = 'CTGYPA'
    category_id = Field('categoryID')
    custom_expression = Field('customExpression')
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    is_invalid_expression = Field('isInvalidExpression')
    is_journaled = Field('isJournaled')
    is_required = Field('isRequired')
    parameter_group_id = Field('parameterGroupID')
    parameter_id = Field('parameterID')
    row_shared = Field('rowShared')
    security_level = Field('securityLevel')
    update_calculated_values = Field('updateCalculatedValues')
    view_security_level = Field('viewSecurityLevel')
    category = Reference('category')
    category_parameter_expression = Reference('categoryParameterExpression')
    customer = Reference('customer')
    parameter = Reference('parameter')
    parameter_group = Reference('parameterGroup')

api.register(CategoryParameter)


class CategoryParameterExpression(Object):
    code = 'CTGPEX'
    custom_expression = Field('customExpression')
    customer_id = Field('customerID')
    has_finance_fields = Field('hasFinanceFields')
    category_parameter = Reference('categoryParameter')
    customer = Reference('customer')

api.register(CategoryParameterExpression)


class Company(Object):
    code = 'CMPY'
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    default_interface = Field('defaultInterface')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_rate_override = Field('hasRateOverride')
    is_primary = Field('isPrimary')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')
    rates = Collection('rates')

    def add_early_access(self, ids=None):
        """
        The ``addEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/addEarlyAccess', params)
        

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def delete_early_access(self, ids=None):
        """
        The ``deleteEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/deleteEarlyAccess', params)
        

    def has_reference(self, ids=None):
        """
        The ``hasReference`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/hasReference', params)
        return data['result']

api.register(Company)


class ComponentKey(Object):
    code = 'CMPSRV'
    component_key = Field('componentKey')
    name = Field('name')

api.register(ComponentKey)


class CustomEnum(Object):
    code = 'CSTEM'
    color = Field('color')
    customer_id = Field('customerID')
    description = Field('description')
    enum_class = Field('enumClass')
    equates_with = Field('equatesWith')
    ext_ref_id = Field('extRefID')
    is_primary = Field('isPrimary')
    label = Field('label')
    value = Field('value')
    value_as_int = Field('valueAsInt')
    value_as_string = Field('valueAsString')
    customer = Reference('customer')
    custom_enum_orders = Collection('customEnumOrders')

    def get_default_op_task_priority_enum(self):
        """
        The ``getDefaultOpTaskPriorityEnum`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDefaultOpTaskPriorityEnum', params)
        return data['result']

    def get_default_project_status_enum(self):
        """
        The ``getDefaultProjectStatusEnum`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDefaultProjectStatusEnum', params)
        return data['result']

    def get_default_severity_enum(self):
        """
        The ``getDefaultSeverityEnum`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDefaultSeverityEnum', params)
        return data['result']

    def get_default_task_priority_enum(self):
        """
        The ``getDefaultTaskPriorityEnum`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDefaultTaskPriorityEnum', params)
        return data['result']

    def get_enum_color(self, enum_class=None, enum_obj_code=None, value=None):
        """
        The ``getEnumColor`` action.
        
        :param enum_class: enumClass (type: ``string``)
        :param enum_obj_code: enumObjCode (type: ``string``)
        :param value: value (type: ``string``)
        :return: ``string``
        """
        params = {}
        if enum_class is not None: params['enumClass'] = enum_class
        if enum_obj_code is not None: params['enumObjCode'] = enum_obj_code
        if value is not None: params['value'] = value
        data = self.session.put(self.api_url()+'/getEnumColor', params)
        return data['result']

    def set_custom_enums(self, type=None, custom_enums=None, replace_with_key_values=None):
        """
        The ``setCustomEnums`` action.
        
        :param type: type (type: ``string``)
        :param custom_enums: customEnums (type: ``string[]``)
        :param replace_with_key_values: replaceWithKeyValues (type: ``map``)
        :return: ``map``
        """
        params = {}
        if type is not None: params['type'] = type
        if custom_enums is not None: params['customEnums'] = custom_enums
        if replace_with_key_values is not None: params['replaceWithKeyValues'] = replace_with_key_values
        data = self.session.put(self.api_url()+'/setCustomEnums', params)
        return data['result']

api.register(CustomEnum)


class CustomEnumOrder(Object):
    code = 'CSTEMO'
    custom_enum_id = Field('customEnumID')
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    is_hidden = Field('isHidden')
    sub_obj_code = Field('subObjCode')
    custom_enum = Reference('customEnum')
    customer = Reference('customer')

api.register(CustomEnumOrder)


class CustomMenu(Object):
    code = 'CSTMNU'
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    is_parent = Field('isParent')
    label = Field('label')
    menu_obj_code = Field('menuObjCode')
    obj_id = Field('objID')
    obj_interface = Field('objInterface')
    target_external_section_id = Field('targetExternalSectionID')
    target_obj_code = Field('targetObjCode')
    target_obj_id = Field('targetObjID')
    target_portal_section_id = Field('targetPortalSectionID')
    target_portal_tab_id = Field('targetPortalTabID')
    window = Field('window')
    customer = Reference('customer')
    portal_profile = Reference('portalProfile')
    target_external_section = Reference('targetExternalSection')
    target_portal_section = Reference('targetPortalSection')
    target_portal_tab = Reference('targetPortalTab')
    children_menus = Collection('childrenMenus')

api.register(CustomMenu)


class CustomMenuCustomMenu(Object):
    code = 'CMSCMS'
    child_id = Field('childID')
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    parent_id = Field('parentID')
    child = Reference('child')
    customer = Reference('customer')
    parent = Reference('parent')

api.register(CustomMenuCustomMenu)


class CustomQuarter(Object):
    code = 'CSTQRT'
    customer_id = Field('customerID')
    end_date = Field('endDate')
    quarter_label = Field('quarterLabel')
    start_date = Field('startDate')
    customer = Reference('customer')

api.register(CustomQuarter)


class Customer(Object):
    code = 'CUST'
    access_rules_per_object_limit = Field('accessRulesPerObjectLimit')
    account_rep_id = Field('accountRepID')
    account_representative = Field('accountRepresentative')
    address = Field('address')
    address2 = Field('address2')
    admin_acct_name = Field('adminAcctName')
    admin_acct_password = Field('adminAcctPassword')
    admin_user_id = Field('adminUserID')
    api_concurrency_limit = Field('apiConcurrencyLimit')
    biz_rule_exclusions = Field('bizRuleExclusions')
    city = Field('city')
    cloneable = Field('cloneable')
    country = Field('country')
    currency = Field('currency')
    custom_enum_types = Field('customEnumTypes')
    customer_config_map_id = Field('customerConfigMapID')
    customer_urlconfig_map_id = Field('customerURLConfigMapID')
    dd_svnversion = Field('ddSVNVersion')
    demo_baseline_date = Field('demoBaselineDate')
    description = Field('description')
    disabled_date = Field('disabledDate')
    document_size = Field('documentSize')
    domain = Field('domain')
    email_addr = Field('emailAddr')
    entry_date = Field('entryDate')
    eval_exp_date = Field('evalExpDate')
    exp_date = Field('expDate')
    ext_ref_id = Field('extRefID')
    external_document_storage = Field('externalDocumentStorage')
    external_users_enabled = Field('externalUsersEnabled')
    external_users_group_id = Field('externalUsersGroupID')
    extra_document_storage = Field('extraDocumentStorage')
    finance_representative = Field('financeRepresentative')
    firstname = Field('firstname')
    full_users = Field('fullUsers')
    golden = Field('golden')
    has_documents = Field('hasDocuments')
    has_preview_access = Field('hasPreviewAccess')
    has_timed_notifications = Field('hasTimedNotifications')
    help_desk_config_map_id = Field('helpDeskConfigMapID')
    inline_java_script_config_map_id = Field('inlineJavaScriptConfigMapID')
    is_apienabled = Field('isAPIEnabled')
    is_advanced_doc_mgmt_enabled = Field('isAdvancedDocMgmtEnabled')
    is_async_reporting_enabled = Field('isAsyncReportingEnabled')
    is_custom_quarter_enabled = Field('isCustomQuarterEnabled')
    is_dam_enabled = Field('isDamEnabled')
    is_disabled = Field('isDisabled')
    is_enterprise = Field('isEnterprise')
    is_migrated_to_anaconda = Field('isMigratedToAnaconda')
    is_portal_profile_migrated = Field('isPortalProfileMigrated')
    is_proofing_enabled = Field('isProofingEnabled')
    is_soapenabled = Field('isSOAPEnabled')
    is_search_enabled = Field('isSearchEnabled')
    is_search_index_active = Field('isSearchIndexActive')
    is_warning_disabled = Field('isWarningDisabled')
    is_white_list_ipenabled = Field('isWhiteListIPEnabled')
    is_workfront_dam_enabled = Field('isWorkfrontDamEnabled')
    journal_field_limit = Field('journalFieldLimit')
    kick_start_expoert_dashboards_limit = Field('kickStartExpoertDashboardsLimit')
    kick_start_expoert_reports_limit = Field('kickStartExpoertReportsLimit')
    last_remind_date = Field('lastRemindDate')
    last_usage_report_date = Field('lastUsageReportDate')
    lastname = Field('lastname')
    limited_users = Field('limitedUsers')
    list_auto_refresh_interval_seconds = Field('listAutoRefreshIntervalSeconds')
    locale = Field('locale')
    lucid_migration_date = Field('lucidMigrationDate')
    lucid_migration_mode = Field('lucidMigrationMode')
    lucid_migration_options = Field('lucidMigrationOptions')
    lucid_migration_status = Field('lucidMigrationStatus')
    lucid_migration_step = Field('lucidMigrationStep')
    name = Field('name')
    need_license_agreement = Field('needLicenseAgreement')
    next_usage_report_date = Field('nextUsageReportDate')
    notification_config_map_id = Field('notificationConfigMapID')
    on_demand_options = Field('onDemandOptions')
    op_task_count_limit = Field('opTaskCountLimit')
    password_config_map_id = Field('passwordConfigMapID')
    phone_number = Field('phoneNumber')
    portfolio_management_config_map_id = Field('portfolioManagementConfigMapID')
    postal_code = Field('postalCode')
    project_management_config_map_id = Field('projectManagementConfigMapID')
    proof_account_id = Field('proofAccountID')
    query_limit = Field('queryLimit')
    record_limit = Field('recordLimit')
    requestor_users = Field('requestorUsers')
    reseller_id = Field('resellerID')
    review_users = Field('reviewUsers')
    sandbox_count = Field('sandboxCount')
    sandbox_refreshing = Field('sandboxRefreshing')
    security_model_type = Field('securityModelType')
    sso_type = Field('ssoType')
    state = Field('state')
    status = Field('status')
    style_sheet = Field('styleSheet')
    task_count_limit = Field('taskCountLimit')
    team_users = Field('teamUsers')
    time_zone = Field('timeZone')
    timesheet_config_map_id = Field('timesheetConfigMapID')
    trial = Field('trial')
    ui_config_map_id = Field('uiConfigMapID')
    usage_report_attempts = Field('usageReportAttempts')
    use_external_document_storage = Field('useExternalDocumentStorage')
    user_invite_config_map_id = Field('userInviteConfigMapID')
    account_rep = Reference('accountRep')
    admin_user = Reference('adminUser')
    customer_config_map = Reference('customerConfigMap')
    customer_urlconfig_map = Reference('customerURLConfigMap')
    external_users_group = Reference('externalUsersGroup')
    help_desk_config_map = Reference('helpDeskConfigMap')
    inline_java_script_config_map = Reference('inlineJavaScriptConfigMap')
    notification_config_map = Reference('notificationConfigMap')
    password_config_map = Reference('passwordConfigMap')
    portfolio_management_config_map = Reference('portfolioManagementConfigMap')
    project_management_config_map = Reference('projectManagementConfigMap')
    reseller = Reference('reseller')
    sso_option = Reference('ssoOption')
    timesheet_config_map = Reference('timesheetConfigMap')
    ui_config_map = Reference('uiConfigMap')
    user_invite_config_map = Reference('userInviteConfigMap')
    access_levels = Collection('accessLevels')
    access_scopes = Collection('accessScopes')
    app_events = Collection('appEvents')
    approval_processes = Collection('approvalProcesses')
    categories = Collection('categories')
    custom_enums = Collection('customEnums')
    custom_menus = Collection('customMenus')
    custom_quarters = Collection('customQuarters')
    custom_tabs = Collection('customTabs')
    customer_prefs = Collection('customerPrefs')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    email_templates = Collection('emailTemplates')
    event_handlers = Collection('eventHandlers')
    expense_types = Collection('expenseTypes')
    external_sections = Collection('externalSections')
    groups = Collection('groups')
    hour_types = Collection('hourTypes')
    import_templates = Collection('importTemplates')
    installed_dditems = Collection('installedDDItems')
    ip_ranges = Collection('ipRanges')
    journal_fields = Collection('journalFields')
    layout_templates = Collection('layoutTemplates')
    license_orders = Collection('licenseOrders')
    milestone_paths = Collection('milestonePaths')
    parameter_groups = Collection('parameterGroups')
    parameters = Collection('parameters')
    portal_profiles = Collection('portalProfiles')
    portal_sections = Collection('portalSections')
    resource_pools = Collection('resourcePools')
    risk_types = Collection('riskTypes')
    roles = Collection('roles')
    schedules = Collection('schedules')
    score_cards = Collection('scoreCards')
    timed_notifications = Collection('timedNotifications')
    ui_filters = Collection('uiFilters')
    ui_group_bys = Collection('uiGroupBys')
    ui_views = Collection('uiViews')

    def accept_license_agreement(self):
        """
        The ``acceptLicenseAgreement`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/acceptLicenseAgreement', params)
        

    def check_license_expiration(self):
        """
        The ``checkLicenseExpiration`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/checkLicenseExpiration', params)
        return data['result']

    def get_license_info(self):
        """
        The ``getLicenseInfo`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getLicenseInfo', params)
        return data['result']

    def is_biz_rule_exclusion_enabled(self, biz_rule=None, obj_code=None, obj_id=None):
        """
        The ``isBizRuleExclusionEnabled`` action.
        
        :param biz_rule: bizRule (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if biz_rule is not None: params['bizRule'] = biz_rule
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/isBizRuleExclusionEnabled', params)
        return data['result']

    def is_ssoenabled(self):
        """
        The ``isSSOEnabled`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/isSSOEnabled', params)
        return data['result']

    def migrate_to_lucid_security(self, migration_mode=None, migration_options=None):
        """
        The ``migrateToLucidSecurity`` action.
        
        :param migration_mode: migrationMode (type: ``com.attask.common.constants.LucidMigrationModeEnum``)
        :param migration_options: migrationOptions (type: ``map``)
        :return: ``string``
        """
        params = {}
        if migration_mode is not None: params['migrationMode'] = migration_mode
        if migration_options is not None: params['migrationOptions'] = migration_options
        data = self.session.put(self.api_url()+'/migrateToLucidSecurity', params)
        return data['result']

    def reset_lucid_security_migration_progress(self):
        """
        The ``resetLucidSecurityMigrationProgress`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/resetLucidSecurityMigrationProgress', params)
        

    def revert_lucid_security_migration(self):
        """
        The ``revertLucidSecurityMigration`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/revertLucidSecurityMigration', params)
        

    def set_exclusions(self, exclusions=None, state=None):
        """
        The ``setExclusions`` action.
        
        :param exclusions: exclusions (type: ``string``)
        :param state: state (type: ``boolean``)
        """
        params = {}
        if exclusions is not None: params['exclusions'] = exclusions
        if state is not None: params['state'] = state
        data = self.session.put(self.api_url()+'/setExclusions', params)
        

    def set_is_custom_quarter_enabled(self, is_custom_quarter_enabled=None):
        """
        The ``setIsCustomQuarterEnabled`` action.
        
        :param is_custom_quarter_enabled: isCustomQuarterEnabled (type: ``boolean``)
        """
        params = {}
        if is_custom_quarter_enabled is not None: params['isCustomQuarterEnabled'] = is_custom_quarter_enabled
        data = self.session.put(self.api_url()+'/setIsCustomQuarterEnabled', params)
        

    def set_is_white_list_ipenabled(self, is_white_list_ipenabled=None):
        """
        The ``setIsWhiteListIPEnabled`` action.
        
        :param is_white_list_ipenabled: isWhiteListIPEnabled (type: ``boolean``)
        """
        params = {}
        if is_white_list_ipenabled is not None: params['isWhiteListIPEnabled'] = is_white_list_ipenabled
        data = self.session.put(self.api_url()+'/setIsWhiteListIPEnabled', params)
        

    def set_lucid_migration_enabled(self, enabled=None):
        """
        The ``setLucidMigrationEnabled`` action.
        
        :param enabled: enabled (type: ``boolean``)
        """
        params = {}
        if enabled is not None: params['enabled'] = enabled
        data = self.session.put(self.api_url()+'/setLucidMigrationEnabled', params)
        

    def update_currency(self, base_currency=None):
        """
        The ``updateCurrency`` action.
        
        :param base_currency: baseCurrency (type: ``string``)
        """
        params = {}
        if base_currency is not None: params['baseCurrency'] = base_currency
        data = self.session.put(self.api_url()+'/updateCurrency', params)
        

    def update_customer_base(self, time_zone=None, locale=None, admin_acct_name=None):
        """
        The ``updateCustomerBase`` action.
        
        :param time_zone: timeZone (type: ``string``)
        :param locale: locale (type: ``string``)
        :param admin_acct_name: adminAcctName (type: ``string``)
        """
        params = {}
        if time_zone is not None: params['timeZone'] = time_zone
        if locale is not None: params['locale'] = locale
        if admin_acct_name is not None: params['adminAcctName'] = admin_acct_name
        data = self.session.put(self.api_url()+'/updateCustomerBase', params)
        

    def update_proofing_billing_plan(self, plan_id=None):
        """
        The ``updateProofingBillingPlan`` action.
        
        :param plan_id: planID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if plan_id is not None: params['planID'] = plan_id
        data = self.session.put(self.api_url()+'/updateProofingBillingPlan', params)
        return data['result']

api.register(Customer)


class CustomerFeedback(Object):
    code = 'CSFD'
    comment = Field('comment')
    customer_guid = Field('customerGUID')
    entry_date = Field('entryDate')
    feedback_type = Field('feedbackType')
    is_admin = Field('isAdmin')
    is_primary_admin = Field('isPrimaryAdmin')
    license_type = Field('licenseType')
    score = Field('score')
    user_guid = Field('userGUID')

api.register(CustomerFeedback)


class CustomerPref(Object):
    code = 'CSTPRF'
    customer_id = Field('customerID')
    pref_name = Field('prefName')
    pref_value = Field('prefValue')
    customer = Reference('customer')

api.register(CustomerPref)


class CustomerPreferences(Object):
    code = 'CUSTPR'
    name = Field('name')
    obj_code = Field('objCode')
    possible_values = Field('possibleValues')
    value = Field('value')

    def set_preference(self, name=None, value=None):
        """
        The ``setPreference`` action.
        
        :param name: name (type: ``string``)
        :param value: value (type: ``string``)
        """
        params = {}
        if name is not None: params['name'] = name
        if value is not None: params['value'] = value
        data = self.session.put(self.api_url()+'/setPreference', params)
        

api.register(CustomerPreferences)


class CustomerTimelineCalc(Object):
    code = 'CPTC'
    customer_id = Field('customerID')
    olv = Field('olv')
    start_date = Field('startDate')
    timeline_calculation_status = Field('timelineCalculationStatus')
    customer = Reference('customer')

api.register(CustomerTimelineCalc)


class CustsSections(Object):
    code = 'CSTSEC'
    customer_id = Field('customerID')
    section_id = Field('sectionID')
    customer = Reference('customer')

api.register(CustsSections)


class DocsFolders(Object):
    code = 'DOCFLD'
    customer_id = Field('customerID')
    document_id = Field('documentID')
    folder_id = Field('folderID')
    customer = Reference('customer')
    document = Reference('document')
    folder = Reference('folder')

api.register(DocsFolders)


class Document(Object):
    code = 'DOCU'
    accessor_ids = Field('accessorIDs')
    advanced_proofing_options = Field('advancedProofingOptions')
    category_id = Field('categoryID')
    checked_out_by_id = Field('checkedOutByID')
    create_proof_flag = Field('createProof')
    current_version_id = Field('currentVersionID')
    customer_id = Field('customerID')
    description = Field('description')
    doc_obj_code = Field('docObjCode')
    document_provider_id = Field('documentProviderID')
    document_request_id = Field('documentRequestID')
    download_url = Field('downloadURL')
    ext_ref_id = Field('extRefID')
    external_integration_type = Field('externalIntegrationType')
    file_type = Field('fileType')
    folder_ids = Field('folderIDs')
    handle = Field('handle')
    has_notes = Field('hasNotes')
    is_dir = Field('isDir')
    is_private = Field('isPrivate')
    is_public = Field('isPublic')
    iteration_id = Field('iterationID')
    last_mod_date = Field('lastModDate')
    last_note_id = Field('lastNoteID')
    last_sync_date = Field('lastSyncDate')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    master_task_id = Field('masterTaskID')
    name = Field('name')
    obj_id = Field('objID')
    op_task_id = Field('opTaskID')
    owner_id = Field('ownerID')
    portfolio_id = Field('portfolioID')
    preview_url = Field('previewURL')
    program_id = Field('programID')
    project_id = Field('projectID')
    public_token = Field('publicToken')
    reference_number = Field('referenceNumber')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    reference_object_closed = Field('referenceObjectClosed')
    reference_object_name = Field('referenceObjectName')
    release_version_id = Field('releaseVersionID')
    security_ancestors_disabled = Field('securityAncestorsDisabled')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    top_doc_obj_code = Field('topDocObjCode')
    top_obj_id = Field('topObjID')
    user_id = Field('userID')
    category = Reference('category')
    checked_out_by = Reference('checkedOutBy')
    current_version = Reference('currentVersion')
    customer = Reference('customer')
    document_request = Reference('documentRequest')
    iteration = Reference('iteration')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    master_task = Reference('masterTask')
    op_task = Reference('opTask')
    owner = Reference('owner')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    release_version = Reference('releaseVersion')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    user = Reference('user')
    access_rules = Collection('accessRules')
    approvals = Collection('approvals')
    awaiting_approvals = Collection('awaitingApprovals')
    folders = Collection('folders')
    groups = Collection('groups')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')
    security_ancestors = Collection('securityAncestors')
    shares = Collection('shares')
    subscribers = Collection('subscribers')
    versions = Collection('versions')

    def build_download_manifest(self, document_idmap=None):
        """
        The ``buildDownloadManifest`` action.
        
        :param document_idmap: documentIDMap (type: ``map``)
        :return: ``string``
        """
        params = {}
        if document_idmap is not None: params['documentIDMap'] = document_idmap
        data = self.session.put(self.api_url()+'/buildDownloadManifest', params)
        return data['result']

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def cancel_document_proof(self, document_version_id=None):
        """
        The ``cancelDocumentProof`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        data = self.session.put(self.api_url()+'/cancelDocumentProof', params)
        

    def check_document_tasks(self):
        """
        The ``checkDocumentTasks`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/checkDocumentTasks', params)
        

    def check_in(self, document_id=None):
        """
        The ``checkIn`` action.
        
        :param document_id: documentID (type: ``string``)
        """
        params = {}
        if document_id is not None: params['documentID'] = document_id
        data = self.session.put(self.api_url()+'/checkIn', params)
        

    def check_out(self, document_id=None):
        """
        The ``checkOut`` action.
        
        :param document_id: documentID (type: ``string``)
        """
        params = {}
        if document_id is not None: params['documentID'] = document_id
        data = self.session.put(self.api_url()+'/checkOut', params)
        

    def copy_document_to_temp_dir(self, document_id=None):
        """
        The ``copyDocumentToTempDir`` action.
        
        :param document_id: documentID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if document_id is not None: params['documentID'] = document_id
        data = self.session.put(self.api_url()+'/copyDocumentToTempDir', params)
        return data['result']

    def create_document(self, name=None, doc_obj_code=None, doc_obj_id=None, file_handle=None, file_type=None, folder_id=None, create_proof=None, advanced_proofing_options=None):
        """
        The ``createDocument`` action.
        
        :param name: name (type: ``string``)
        :param doc_obj_code: docObjCode (type: ``string``)
        :param doc_obj_id: docObjID (type: ``string``)
        :param file_handle: fileHandle (type: ``string``)
        :param file_type: fileType (type: ``string``)
        :param folder_id: folderID (type: ``string``)
        :param create_proof: createProof (type: ``java.lang.Boolean``)
        :param advanced_proofing_options: advancedProofingOptions (type: ``string``)
        :return: ``string``
        """
        params = {}
        if name is not None: params['name'] = name
        if doc_obj_code is not None: params['docObjCode'] = doc_obj_code
        if doc_obj_id is not None: params['docObjID'] = doc_obj_id
        if file_handle is not None: params['fileHandle'] = file_handle
        if file_type is not None: params['fileType'] = file_type
        if folder_id is not None: params['folderID'] = folder_id
        if create_proof is not None: params['createProof'] = create_proof
        if advanced_proofing_options is not None: params['advancedProofingOptions'] = advanced_proofing_options
        data = self.session.put(self.api_url()+'/createDocument', params)
        return data['result']

    def create_proof(self, document_version_id=None, advanced_proofing_options=None):
        """
        The ``createProof`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        :param advanced_proofing_options: advancedProofingOptions (type: ``string``)
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        if advanced_proofing_options is not None: params['advancedProofingOptions'] = advanced_proofing_options
        data = self.session.put(self.api_url()+'/createProof', params)
        

    def delete_document_proofs(self, document_id=None):
        """
        The ``deleteDocumentProofs`` action.
        
        :param document_id: documentID (type: ``string``)
        """
        params = {}
        if document_id is not None: params['documentID'] = document_id
        data = self.session.put(self.api_url()+'/deleteDocumentProofs', params)
        

    def get_advanced_proof_options_url(self):
        """
        The ``getAdvancedProofOptionsURL`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getAdvancedProofOptionsURL', params)
        return data['result']

    def get_document_contents_in_zip(self):
        """
        The ``getDocumentContentsInZip`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getDocumentContentsInZip', params)
        return data['result']

    def get_external_document_contents(self):
        """
        The ``getExternalDocumentContents`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getExternalDocumentContents', params)
        return data['result']

    def get_generic_thumbnail_url(self, document_version_id=None):
        """
        The ``getGenericThumbnailUrl`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        data = self.session.put(self.api_url()+'/getGenericThumbnailUrl', params)
        return data['result']

    def get_proof_details(self, document_version_id=None):
        """
        The ``getProofDetails`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        :return: ``map``
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        data = self.session.put(self.api_url()+'/getProofDetails', params)
        return data['result']

    def get_proof_details_url(self, proof_id=None):
        """
        The ``getProofDetailsURL`` action.
        
        :param proof_id: proofID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if proof_id is not None: params['proofID'] = proof_id
        data = self.session.put(self.api_url()+'/getProofDetailsURL', params)
        return data['result']

    def get_proof_url(self):
        """
        The ``getProofURL`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getProofURL', params)
        return data['result']

    def get_proof_usage(self):
        """
        The ``getProofUsage`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getProofUsage', params)
        return data['result']

    def get_public_generic_thumbnail_url(self, document_version_id=None, public_token=None):
        """
        The ``getPublicGenericThumbnailUrl`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        :param public_token: publicToken (type: ``string``)
        :return: ``string``
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        if public_token is not None: params['publicToken'] = public_token
        data = self.session.put(self.api_url()+'/getPublicGenericThumbnailUrl', params)
        return data['result']

    def get_public_thumbnail_file_path(self, document_version_id=None, size=None, public_token=None):
        """
        The ``getPublicThumbnailFilePath`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        :param size: size (type: ``string``)
        :param public_token: publicToken (type: ``string``)
        :return: ``string``
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        if size is not None: params['size'] = size
        if public_token is not None: params['publicToken'] = public_token
        data = self.session.put(self.api_url()+'/getPublicThumbnailFilePath', params)
        return data['result']

    def get_s3document_url(self, content_disposition=None, external_storage_id=None, customer_prefs=None):
        """
        The ``getS3DocumentURL`` action.
        
        :param content_disposition: contentDisposition (type: ``string``)
        :param external_storage_id: externalStorageID (type: ``string``)
        :param customer_prefs: customerPrefs (type: ``map``)
        :return: ``string``
        """
        params = {}
        if content_disposition is not None: params['contentDisposition'] = content_disposition
        if external_storage_id is not None: params['externalStorageID'] = external_storage_id
        if customer_prefs is not None: params['customerPrefs'] = customer_prefs
        data = self.session.put(self.api_url()+'/getS3DocumentURL', params)
        return data['result']

    def get_thumbnail_data(self, document_version_id=None, size=None):
        """
        The ``getThumbnailData`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        :param size: size (type: ``string``)
        :return: ``string``
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        if size is not None: params['size'] = size
        data = self.session.put(self.api_url()+'/getThumbnailData', params)
        return data['result']

    def get_thumbnail_file_path(self, document_version_id=None, size=None):
        """
        The ``getThumbnailFilePath`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        :param size: size (type: ``string``)
        :return: ``string``
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        if size is not None: params['size'] = size
        data = self.session.put(self.api_url()+'/getThumbnailFilePath', params)
        return data['result']

    def get_total_size_for_documents(self, document_ids=None, include_linked=None):
        """
        The ``getTotalSizeForDocuments`` action.
        
        :param document_ids: documentIDs (type: ``string[]``)
        :param include_linked: includeLinked (type: ``boolean``)
        :return: ``java.lang.Long``
        """
        params = {}
        if document_ids is not None: params['documentIDs'] = document_ids
        if include_linked is not None: params['includeLinked'] = include_linked
        data = self.session.put(self.api_url()+'/getTotalSizeForDocuments', params)
        return data['result']

    def handle_proof_callback(self, callback_xml=None):
        """
        The ``handleProofCallback`` action.
        
        :param callback_xml: callbackXML (type: ``string``)
        """
        params = {}
        if callback_xml is not None: params['callbackXML'] = callback_xml
        data = self.session.put(self.api_url()+'/handleProofCallback', params)
        

    def is_in_linked_folder(self, document_id=None):
        """
        The ``isInLinkedFolder`` action.
        
        :param document_id: documentID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if document_id is not None: params['documentID'] = document_id
        data = self.session.put(self.api_url()+'/isInLinkedFolder', params)
        return data['result']

    def is_linked_document(self, document_id=None):
        """
        The ``isLinkedDocument`` action.
        
        :param document_id: documentID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if document_id is not None: params['documentID'] = document_id
        data = self.session.put(self.api_url()+'/isLinkedDocument', params)
        return data['result']

    def is_proof_auto_genration_enabled(self):
        """
        The ``isProofAutoGenrationEnabled`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/isProofAutoGenrationEnabled', params)
        return data['result']

    def is_proofable(self, document_version_id=None):
        """
        The ``isProofable`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        data = self.session.put(self.api_url()+'/isProofable', params)
        return data['result']

    def move(self, obj_id=None, doc_obj_code=None):
        """
        The ``move`` action.
        
        :param obj_id: objID (type: ``string``)
        :param doc_obj_code: docObjCode (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if doc_obj_code is not None: params['docObjCode'] = doc_obj_code
        data = self.session.put(self.api_url()+'/move', params)
        

    def process_google_drive_change_notification(self, push_notification=None):
        """
        The ``processGoogleDriveChangeNotification`` action.
        
        :param push_notification: pushNotification (type: ``string``)
        """
        params = {}
        if push_notification is not None: params['pushNotification'] = push_notification
        data = self.session.put(self.api_url()+'/processGoogleDriveChangeNotification', params)
        

    def refresh_external_document_info(self, document_id=None):
        """
        The ``refreshExternalDocumentInfo`` action.
        
        :param document_id: documentID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if document_id is not None: params['documentID'] = document_id
        data = self.session.put(self.api_url()+'/refreshExternalDocumentInfo', params)
        return data['result']

    def refresh_external_documents(self):
        """
        The ``refreshExternalDocuments`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/refreshExternalDocuments', params)
        

    def regenerate_box_shared_link(self, document_version_id=None):
        """
        The ``regenerateBoxSharedLink`` action.
        
        :param document_version_id: documentVersionID (type: ``string``)
        """
        params = {}
        if document_version_id is not None: params['documentVersionID'] = document_version_id
        data = self.session.put(self.api_url()+'/regenerateBoxSharedLink', params)
        

    def remind_requestee(self, document_request_id=None):
        """
        The ``remindRequestee`` action.
        
        :param document_request_id: documentRequestID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if document_request_id is not None: params['documentRequestID'] = document_request_id
        data = self.session.put(self.api_url()+'/remindRequestee', params)
        return data['result']

    def save_document_metadata(self, document_id=None):
        """
        The ``saveDocumentMetadata`` action.
        
        :param document_id: documentID (type: ``string``)
        """
        params = {}
        if document_id is not None: params['documentID'] = document_id
        data = self.session.put(self.api_url()+'/saveDocumentMetadata', params)
        

    def send_documents_to_external_provider(self, document_ids=None, provider_id=None, destination_folder_id=None):
        """
        The ``sendDocumentsToExternalProvider`` action.
        
        :param document_ids: documentIDs (type: ``string[]``)
        :param provider_id: providerID (type: ``string``)
        :param destination_folder_id: destinationFolderID (type: ``string``)
        """
        params = {}
        if document_ids is not None: params['documentIDs'] = document_ids
        if provider_id is not None: params['providerID'] = provider_id
        if destination_folder_id is not None: params['destinationFolderID'] = destination_folder_id
        data = self.session.put(self.api_url()+'/sendDocumentsToExternalProvider', params)
        

    def setup_google_drive_push_notifications(self):
        """
        The ``setupGoogleDrivePushNotifications`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/setupGoogleDrivePushNotifications', params)
        return data['result']

    def unlink_documents(self, ids=None):
        """
        The ``unlinkDocuments`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/unlinkDocuments', params)
        return data['result']

    def upload_documents(self, document_request_id=None, documents=None):
        """
        The ``uploadDocuments`` action.
        
        :param document_request_id: documentRequestID (type: ``string``)
        :param documents: documents (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if document_request_id is not None: params['documentRequestID'] = document_request_id
        if documents is not None: params['documents'] = documents
        data = self.session.put(self.api_url()+'/uploadDocuments', params)
        return data['result']

    def zip_document_versions(self):
        """
        The ``zipDocumentVersions`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/zipDocumentVersions', params)
        return data['result']

    def zip_documents(self, obj_code=None, obj_id=None):
        """
        The ``zipDocuments`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/zipDocuments', params)
        return data['result']

    def zip_documents_versions(self, ids=None):
        """
        The ``zipDocumentsVersions`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``string``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/zipDocumentsVersions', params)
        return data['result']

api.register(Document)


class DocumentApproval(Object):
    code = 'DOCAPL'
    approval_date = Field('approvalDate')
    approver_id = Field('approverID')
    auto_document_share_id = Field('autoDocumentShareID')
    customer_id = Field('customerID')
    document_id = Field('documentID')
    note_id = Field('noteID')
    request_date = Field('requestDate')
    requestor_id = Field('requestorID')
    status = Field('status')
    approver = Reference('approver')
    auto_document_share = Reference('autoDocumentShare')
    customer = Reference('customer')
    document = Reference('document')
    note = Reference('note')
    requestor = Reference('requestor')

    def notify_approver(self, id=None):
        """
        The ``notifyApprover`` action.
        
        :param id: ID (type: ``string``)
        """
        params = {}
        if id is not None: params['ID'] = id
        data = self.session.put(self.api_url()+'/notifyApprover', params)
        

api.register(DocumentApproval)


class DocumentFolder(Object):
    code = 'DOCFDR'
    accessor_ids = Field('accessorIDs')
    customer_id = Field('customerID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    issue_id = Field('issueID')
    iteration_id = Field('iterationID')
    last_mod_date = Field('lastModDate')
    linked_folder_id = Field('linkedFolderID')
    name = Field('name')
    parent_id = Field('parentID')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    user_id = Field('userID')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    issue = Reference('issue')
    iteration = Reference('iteration')
    linked_folder = Reference('linkedFolder')
    parent = Reference('parent')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    user = Reference('user')
    children = Collection('children')
    documents = Collection('documents')

    def delete_folders_and_contents(self, document_folder_id=None, obj_code=None, object_id=None):
        """
        The ``deleteFoldersAndContents`` action.
        
        :param document_folder_id: documentFolderID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param object_id: objectID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if document_folder_id is not None: params['documentFolderID'] = document_folder_id
        if obj_code is not None: params['objCode'] = obj_code
        if object_id is not None: params['objectID'] = object_id
        data = self.session.put(self.api_url()+'/deleteFoldersAndContents', params)
        return data['result']

    def get_folder_size_in_bytes(self, folder_id=None, recursive=None, include_linked=None):
        """
        The ``getFolderSizeInBytes`` action.
        
        :param folder_id: folderID (type: ``string``)
        :param recursive: recursive (type: ``boolean``)
        :param include_linked: includeLinked (type: ``boolean``)
        :return: ``java.lang.Long``
        """
        params = {}
        if folder_id is not None: params['folderID'] = folder_id
        if recursive is not None: params['recursive'] = recursive
        if include_linked is not None: params['includeLinked'] = include_linked
        data = self.session.put(self.api_url()+'/getFolderSizeInBytes', params)
        return data['result']

    def get_linked_folder_meta_data(self, linked_folder_id=None):
        """
        The ``getLinkedFolderMetaData`` action.
        
        :param linked_folder_id: linkedFolderID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if linked_folder_id is not None: params['linkedFolderID'] = linked_folder_id
        data = self.session.put(self.api_url()+'/getLinkedFolderMetaData', params)
        return data['result']

    def is_linked_folder(self, document_folder_id=None):
        """
        The ``isLinkedFolder`` action.
        
        :param document_folder_id: documentFolderID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if document_folder_id is not None: params['documentFolderID'] = document_folder_id
        data = self.session.put(self.api_url()+'/isLinkedFolder', params)
        return data['result']

    def is_smart_folder(self, document_folder_id=None):
        """
        The ``isSmartFolder`` action.
        
        :param document_folder_id: documentFolderID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if document_folder_id is not None: params['documentFolderID'] = document_folder_id
        data = self.session.put(self.api_url()+'/isSmartFolder', params)
        return data['result']

    def refresh_linked_folder(self, linked_folder_id=None, obj_code=None, object_id=None):
        """
        The ``refreshLinkedFolder`` action.
        
        :param linked_folder_id: linkedFolderID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param object_id: objectID (type: ``string``)
        """
        params = {}
        if linked_folder_id is not None: params['linkedFolderID'] = linked_folder_id
        if obj_code is not None: params['objCode'] = obj_code
        if object_id is not None: params['objectID'] = object_id
        data = self.session.put(self.api_url()+'/refreshLinkedFolder', params)
        

    def refresh_linked_folder_contents(self, linked_folder_id=None, obj_code=None, object_id=None):
        """
        The ``refreshLinkedFolderContents`` action.
        
        :param linked_folder_id: linkedFolderID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param object_id: objectID (type: ``string``)
        """
        params = {}
        if linked_folder_id is not None: params['linkedFolderID'] = linked_folder_id
        if obj_code is not None: params['objCode'] = obj_code
        if object_id is not None: params['objectID'] = object_id
        data = self.session.put(self.api_url()+'/refreshLinkedFolderContents', params)
        

    def refresh_linked_folder_meta_data(self, linked_folder_id=None):
        """
        The ``refreshLinkedFolderMetaData`` action.
        
        :param linked_folder_id: linkedFolderID (type: ``string``)
        """
        params = {}
        if linked_folder_id is not None: params['linkedFolderID'] = linked_folder_id
        data = self.session.put(self.api_url()+'/refreshLinkedFolderMetaData', params)
        

    def send_folder_to_external_provider(self, folder_id=None, document_provider_id=None, parent_external_storage_id=None):
        """
        The ``sendFolderToExternalProvider`` action.
        
        :param folder_id: folderID (type: ``string``)
        :param document_provider_id: documentProviderID (type: ``string``)
        :param parent_external_storage_id: parentExternalStorageID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if folder_id is not None: params['folderID'] = folder_id
        if document_provider_id is not None: params['documentProviderID'] = document_provider_id
        if parent_external_storage_id is not None: params['parentExternalStorageID'] = parent_external_storage_id
        data = self.session.put(self.api_url()+'/sendFolderToExternalProvider', params)
        return data['result']

    def unlink_folders(self, ids=None):
        """
        The ``unlinkFolders`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/unlinkFolders', params)
        return data['result']

api.register(DocumentFolder)


class DocumentProvider(Object):
    code = 'DOCPRO'
    configuration = Field('configuration')
    customer_id = Field('customerID')
    doc_provider_config_id = Field('docProviderConfigID')
    entry_date = Field('entryDate')
    external_integration_type = Field('externalIntegrationType')
    name = Field('name')
    owner_id = Field('ownerID')
    web_hook_expiration_date = Field('webHookExpirationDate')
    customer = Reference('customer')
    doc_provider_config = Reference('docProviderConfig')
    owner = Reference('owner')

    def get_all_type_provider_ids(self, external_integration_type=None, doc_provider_config_id=None):
        """
        The ``getAllTypeProviderIDs`` action.
        
        :param external_integration_type: externalIntegrationType (type: ``string``)
        :param doc_provider_config_id: docProviderConfigID (type: ``string``)
        :return: ``string[]``
        """
        params = {}
        if external_integration_type is not None: params['externalIntegrationType'] = external_integration_type
        if doc_provider_config_id is not None: params['docProviderConfigID'] = doc_provider_config_id
        data = self.session.put(self.api_url()+'/getAllTypeProviderIDs', params)
        return data['result']

    def get_provider_with_write_access(self, external_integration_type=None, config_id=None, external_folder_id=None):
        """
        The ``getProviderWithWriteAccess`` action.
        
        :param external_integration_type: externalIntegrationType (type: ``string``)
        :param config_id: configID (type: ``string``)
        :param external_folder_id: externalFolderID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if external_integration_type is not None: params['externalIntegrationType'] = external_integration_type
        if config_id is not None: params['configID'] = config_id
        if external_folder_id is not None: params['externalFolderID'] = external_folder_id
        data = self.session.put(self.api_url()+'/getProviderWithWriteAccess', params)
        return data['result']

api.register(DocumentProvider)


class DocumentProviderConfig(Object):
    code = 'DOCCFG'
    configuration = Field('configuration')
    customer_id = Field('customerID')
    external_integration_type = Field('externalIntegrationType')
    host = Field('host')
    is_active = Field('isActive')
    name = Field('name')
    customer = Reference('customer')

api.register(DocumentProviderConfig)


class DocumentProviderMetadata(Object):
    code = 'DOCMET'
    customer_id = Field('customerID')
    external_integration_type = Field('externalIntegrationType')
    mapping = Field('mapping')
    customer = Reference('customer')

    def get_metadata_map_for_provider_type(self, external_integration_type=None):
        """
        The ``getMetadataMapForProviderType`` action.
        
        :param external_integration_type: externalIntegrationType (type: ``string``)
        :return: ``map``
        """
        params = {}
        if external_integration_type is not None: params['externalIntegrationType'] = external_integration_type
        data = self.session.put(self.api_url()+'/getMetadataMapForProviderType', params)
        return data['result']

    def load_metadata_for_document(self, document_id=None, external_integration_type=None):
        """
        The ``loadMetadataForDocument`` action.
        
        :param document_id: documentID (type: ``string``)
        :param external_integration_type: externalIntegrationType (type: ``string``)
        :return: ``map``
        """
        params = {}
        if document_id is not None: params['documentID'] = document_id
        if external_integration_type is not None: params['externalIntegrationType'] = external_integration_type
        data = self.session.put(self.api_url()+'/loadMetadataForDocument', params)
        return data['result']

api.register(DocumentProviderMetadata)


class DocumentRequest(Object):
    code = 'DOCREQ'
    accessor_ids = Field('accessorIDs')
    completion_date = Field('completionDate')
    customer_id = Field('customerID')
    description = Field('description')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    format_entry_date = Field('formatEntryDate')
    iteration_id = Field('iterationID')
    master_task_id = Field('masterTaskID')
    op_task_id = Field('opTaskID')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    ref_obj_code = Field('refObjCode')
    ref_obj_id = Field('refObjID')
    requestee_id = Field('requesteeID')
    requestor_id = Field('requestorID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    status = Field('status')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    user_id = Field('userID')
    customer = Reference('customer')
    iteration = Reference('iteration')
    master_task = Reference('masterTask')
    op_task = Reference('opTask')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    requestee = Reference('requestee')
    requestor = Reference('requestor')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    user = Reference('user')

api.register(DocumentRequest)


class DocumentShare(Object):
    code = 'DOCSHR'
    accessor_ids = Field('accessorIDs')
    accessor_obj_code = Field('accessorObjCode')
    accessor_obj_id = Field('accessorObjID')
    customer_id = Field('customerID')
    description = Field('description')
    document_id = Field('documentID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    is_approver = Field('isApprover')
    is_download = Field('isDownload')
    is_proofer = Field('isProofer')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    role_id = Field('roleID')
    team_id = Field('teamID')
    user_id = Field('userID')
    customer = Reference('customer')
    document = Reference('document')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    pending_approval = Reference('pendingApproval')
    role = Reference('role')
    team = Reference('team')
    user = Reference('user')

    def notify_share(self, id=None):
        """
        The ``notifyShare`` action.
        
        :param id: ID (type: ``string``)
        """
        params = {}
        if id is not None: params['ID'] = id
        data = self.session.put(self.api_url()+'/notifyShare', params)
        

api.register(DocumentShare)


class DocumentTaskStatus(Object):
    code = 'DOCTSK'
    customer_id = Field('customerID')
    document_version_id = Field('documentVersionID')
    file_path = Field('filePath')
    service_name = Field('serviceName')
    status = Field('status')
    status_date = Field('statusDate')
    task_info = Field('taskInfo')
    user_id = Field('userID')

api.register(DocumentTaskStatus)


class DocumentVersion(Object):
    code = 'DOCV'
    accessor_ids = Field('accessorIDs')
    advanced_proofing_options = Field('advancedProofingOptions')
    create_proof = Field('createProof')
    customer_id = Field('customerID')
    doc_size = Field('docSize')
    doc_status = Field('docStatus')
    document_id = Field('documentID')
    document_provider_id = Field('documentProviderID')
    document_type_label = Field('documentTypeLabel')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext = Field('ext')
    external_download_url = Field('externalDownloadURL')
    external_integration_type = Field('externalIntegrationType')
    external_preview_url = Field('externalPreviewURL')
    external_save_location = Field('externalSaveLocation')
    external_storage_id = Field('externalStorageID')
    file_name = Field('fileName')
    file_type = Field('fileType')
    format_doc_size = Field('formatDocSize')
    format_entry_date = Field('formatEntryDate')
    handle = Field('handle')
    icon = Field('icon')
    is_proof_automated = Field('isProofAutomated')
    is_proofable = Field('isProofable')
    location = Field('location')
    proof_id = Field('proofID')
    proof_stage_id = Field('proofStageID')
    proof_status = Field('proofStatus')
    proof_status_date = Field('proofStatusDate')
    proof_status_msg_key = Field('proofStatusMsgKey')
    version = Field('version')
    virus_scan = Field('virusScan')
    virus_scan_timestamp = Field('virusScanTimestamp')
    customer = Reference('customer')
    document = Reference('document')
    document_provider = Reference('documentProvider')
    entered_by = Reference('enteredBy')

    def add_document_version(self, document_version_bean=None):
        """
        The ``addDocumentVersion`` action.
        
        :param document_version_bean: documentVersionBean (type: ``DocumentVersion``)
        :return: ``string``
        """
        params = {}
        if document_version_bean is not None: params['documentVersionBean'] = document_version_bean
        data = self.session.put(self.api_url()+'/addDocumentVersion', params)
        return data['result']

    def file_handle(self):
        """
        The ``fileHandle`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/fileHandle', params)
        return data['result']

    def public_file_handle(self, version_id=None, public_token=None):
        """
        The ``publicFileHandle`` action.
        
        :param version_id: versionID (type: ``string``)
        :param public_token: publicToken (type: ``string``)
        :return: ``string``
        """
        params = {}
        if version_id is not None: params['versionID'] = version_id
        if public_token is not None: params['publicToken'] = public_token
        data = self.session.put(self.api_url()+'/publicFileHandle', params)
        return data['result']

    def remove_document_version(self, document_version=None):
        """
        The ``removeDocumentVersion`` action.
        
        :param document_version: documentVersion (type: ``DocumentVersion``)
        """
        params = {}
        if document_version is not None: params['documentVersion'] = document_version
        data = self.session.put(self.api_url()+'/removeDocumentVersion', params)
        

api.register(DocumentVersion)


class Email(Object):
    code = 'EMAILC'
    obj_code = Field('objCode')

    def send_test_email(self, email_address=None, username=None, password=None, host=None, port=None, usessl=None):
        """
        The ``sendTestEmail`` action.
        
        :param email_address: emailAddress (type: ``string``)
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param host: host (type: ``string``)
        :param port: port (type: ``string``)
        :param usessl: usessl (type: ``java.lang.Boolean``)
        :return: ``string``
        """
        params = {}
        if email_address is not None: params['emailAddress'] = email_address
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if host is not None: params['host'] = host
        if port is not None: params['port'] = port
        if usessl is not None: params['usessl'] = usessl
        data = self.session.put(self.api_url()+'/sendTestEmail', params)
        return data['result']

    def test_pop_account_settings(self, username=None, password=None, host=None, port=None, usessl=None):
        """
        The ``testPopAccountSettings`` action.
        
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param host: host (type: ``string``)
        :param port: port (type: ``string``)
        :param usessl: usessl (type: ``boolean``)
        :return: ``string``
        """
        params = {}
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if host is not None: params['host'] = host
        if port is not None: params['port'] = port
        if usessl is not None: params['usessl'] = usessl
        data = self.session.put(self.api_url()+'/testPopAccountSettings', params)
        return data['result']

api.register(Email)


class EmailTemplate(Object):
    code = 'EMLTPL'
    content = Field('content')
    customer_id = Field('customerID')
    description = Field('description')
    name = Field('name')
    subject = Field('subject')
    template_obj_code = Field('templateObjCode')
    customer = Reference('customer')

    def get_email_subjects(self, customer_id=None, handler_name_map=None, obj_code=None, obj_id=None, event_type=None):
        """
        The ``getEmailSubjects`` action.
        
        :param customer_id: customerID (type: ``string``)
        :param handler_name_map: handlerNameMap (type: ``map``)
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :param event_type: eventType (type: ``string``)
        :return: ``map``
        """
        params = {}
        if customer_id is not None: params['customerID'] = customer_id
        if handler_name_map is not None: params['handlerNameMap'] = handler_name_map
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        if event_type is not None: params['eventType'] = event_type
        data = self.session.put(self.api_url()+'/getEmailSubjects', params)
        return data['result']

    def get_help_desk_registration_email(self, user_id=None):
        """
        The ``getHelpDeskRegistrationEmail`` action.
        
        :param user_id: userID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/getHelpDeskRegistrationEmail', params)
        return data['result']

    def get_user_invitation_email(self, user_id=None):
        """
        The ``getUserInvitationEmail`` action.
        
        :param user_id: userID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/getUserInvitationEmail', params)
        return data['result']

api.register(EmailTemplate)


class Endorsement(Object):
    code = 'ENDR'
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    has_replies = Field('hasReplies')
    is_assignee = Field('isAssignee')
    is_owner = Field('isOwner')
    num_likes = Field('numLikes')
    num_replies = Field('numReplies')
    op_task_id = Field('opTaskID')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    receiver_id = Field('receiverID')
    ref_obj_code = Field('refObjCode')
    ref_obj_id = Field('refObjID')
    reference_object_name = Field('referenceObjectName')
    role_id = Field('roleID')
    sub_obj_code = Field('subObjCode')
    sub_obj_id = Field('subObjID')
    sub_reference_object_name = Field('subReferenceObjectName')
    task_id = Field('taskID')
    top_obj_code = Field('topObjCode')
    top_obj_id = Field('topObjID')
    top_reference_object_name = Field('topReferenceObjectName')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    op_task = Reference('opTask')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    receiver = Reference('receiver')
    role = Reference('role')
    task = Reference('task')
    replies = Collection('replies')
    shares = Collection('shares')

    def get_liked_endorsement_ids(self, endorsement_ids=None):
        """
        The ``getLikedEndorsementIDs`` action.
        
        :param endorsement_ids: endorsementIDs (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if endorsement_ids is not None: params['endorsementIDs'] = endorsement_ids
        data = self.session.put(self.api_url()+'/getLikedEndorsementIDs', params)
        return data['result']

    def like(self):
        """
        The ``like`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/like', params)
        

    def unlike(self):
        """
        The ``unlike`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unlike', params)
        

api.register(Endorsement)


class EndorsementShare(Object):
    code = 'ENDSHR'
    accessor_obj_code = Field('accessorObjCode')
    accessor_obj_id = Field('accessorObjID')
    customer_id = Field('customerID')
    endorsement_id = Field('endorsementID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    team_id = Field('teamID')
    user_id = Field('userID')
    customer = Reference('customer')
    endorsement = Reference('endorsement')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    team = Reference('team')
    user = Reference('user')

api.register(EndorsementShare)


class EventHandler(Object):
    code = 'EVNTH'
    always_active = Field('alwaysActive')
    custom_properties = Field('customProperties')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    display_subject_value = Field('displaySubjectValue')
    event_obj_code = Field('eventObjCode')
    event_types = Field('eventTypes')
    handler_properties = Field('handlerProperties')
    handler_type = Field('handlerType')
    is_active = Field('isActive')
    is_hidden = Field('isHidden')
    is_system_handler = Field('isSystemHandler')
    name = Field('name')
    name_key = Field('nameKey')
    customer = Reference('customer')
    app_events = Collection('appEvents')

    def reset_subjects_to_default(self, event_handler_ids=None):
        """
        The ``resetSubjectsToDefault`` action.
        
        :param event_handler_ids: eventHandlerIDs (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if event_handler_ids is not None: params['eventHandlerIDs'] = event_handler_ids
        data = self.session.put(self.api_url()+'/resetSubjectsToDefault', params)
        return data['result']

    def set_custom_subject(self, custom_subjects=None, custom_subject_properties=None):
        """
        The ``setCustomSubject`` action.
        
        :param custom_subjects: customSubjects (type: ``string[]``)
        :param custom_subject_properties: customSubjectProperties (type: ``string[]``)
        :return: ``string``
        """
        params = {}
        if custom_subjects is not None: params['customSubjects'] = custom_subjects
        if custom_subject_properties is not None: params['customSubjectProperties'] = custom_subject_properties
        data = self.session.put(self.api_url()+'/setCustomSubject', params)
        return data['result']

api.register(EventHandler)


class EventSubscription(Object):
    code = 'EVTSUB'
    customer_id = Field('customerID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    event_type = Field('eventType')
    last_update_date = Field('lastUpdateDate')
    notification_url = Field('notificationURL')
    status = Field('status')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')

api.register(EventSubscription)


class ExchangeRate(Object):
    code = 'EXRATE'
    accessor_ids = Field('accessorIDs')
    currency = Field('currency')
    customer_id = Field('customerID')
    ext_ref_id = Field('extRefID')
    project_id = Field('projectID')
    rate = Field('rate')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    template_id = Field('templateID')
    customer = Reference('customer')
    project = Reference('project')
    template = Reference('template')

    def suggest_exchange_rate(self, base_currency=None, to_currency_code=None):
        """
        The ``suggestExchangeRate`` action.
        
        :param base_currency: baseCurrency (type: ``string``)
        :param to_currency_code: toCurrencyCode (type: ``string``)
        :return: ``java.lang.Double``
        """
        params = {}
        if base_currency is not None: params['baseCurrency'] = base_currency
        if to_currency_code is not None: params['toCurrencyCode'] = to_currency_code
        data = self.session.put(self.api_url()+'/suggestExchangeRate', params)
        return data['result']

api.register(ExchangeRate)


class Expense(Object):
    code = 'EXPNS'
    accessor_ids = Field('accessorIDs')
    actual_amount = Field('actualAmount')
    actual_unit_amount = Field('actualUnitAmount')
    billing_record_id = Field('billingRecordID')
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    description = Field('description')
    effective_date = Field('effectiveDate')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    exp_obj_code = Field('expObjCode')
    expense_type_id = Field('expenseTypeID')
    ext_ref_id = Field('extRefID')
    is_billable = Field('isBillable')
    is_reimbursable = Field('isReimbursable')
    is_reimbursed = Field('isReimbursed')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    master_task_id = Field('masterTaskID')
    obj_id = Field('objID')
    planned_amount = Field('plannedAmount')
    planned_date = Field('plannedDate')
    planned_unit_amount = Field('plannedUnitAmount')
    project_id = Field('projectID')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    reference_object_name = Field('referenceObjectName')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    top_obj_code = Field('topObjCode')
    top_obj_id = Field('topObjID')
    top_reference_obj_code = Field('topReferenceObjCode')
    top_reference_obj_id = Field('topReferenceObjID')
    billing_record = Reference('billingRecord')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    expense_type = Reference('expenseType')
    last_updated_by = Reference('lastUpdatedBy')
    master_task = Reference('masterTask')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def move(self, obj_id=None, exp_obj_code=None):
        """
        The ``move`` action.
        
        :param obj_id: objID (type: ``string``)
        :param exp_obj_code: expObjCode (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if exp_obj_code is not None: params['expObjCode'] = exp_obj_code
        data = self.session.put(self.api_url()+'/move', params)
        

api.register(Expense)


class ExpenseType(Object):
    code = 'EXPTYP'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    display_per = Field('displayPer')
    display_rate_unit = Field('displayRateUnit')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    rate = Field('rate')
    rate_unit = Field('rateUnit')
    app_global = Reference('appGlobal')
    customer = Reference('customer')

    def has_reference(self, ids=None):
        """
        The ``hasReference`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/hasReference', params)
        return data['result']

api.register(ExpenseType)


class ExternalDocument(Object):
    code = 'EXTDOC'
    allowed_actions = Field('allowedActions')
    date_modified = Field('dateModified')
    description = Field('description')
    document_provider_id = Field('documentProviderID')
    download_url = Field('downloadURL')
    ext = Field('ext')
    file_type = Field('fileType')
    icon_url = Field('iconURL')
    name = Field('name')
    path = Field('path')
    preview_url = Field('previewURL')
    provider_type = Field('providerType')
    read_only = Field('readOnly')
    size = Field('size')
    thumbnail_url = Field('thumbnailURL')

    def browse_list_with_link_action(self, provider_type=None, document_provider_id=None, search_params=None, link_action=None):
        """
        The ``browseListWithLinkAction`` action.
        
        :param provider_type: providerType (type: ``string``)
        :param document_provider_id: documentProviderID (type: ``string``)
        :param search_params: searchParams (type: ``map``)
        :param link_action: linkAction (type: ``string``)
        :return: ``map``
        """
        params = {}
        if provider_type is not None: params['providerType'] = provider_type
        if document_provider_id is not None: params['documentProviderID'] = document_provider_id
        if search_params is not None: params['searchParams'] = search_params
        if link_action is not None: params['linkAction'] = link_action
        data = self.session.put(self.api_url()+'/browseListWithLinkAction', params)
        return data['result']

    def get_authentication_url_for_provider(self, provider_type=None, document_provider_id=None, document_provider_config_id=None):
        """
        The ``getAuthenticationUrlForProvider`` action.
        
        :param provider_type: providerType (type: ``string``)
        :param document_provider_id: documentProviderID (type: ``string``)
        :param document_provider_config_id: documentProviderConfigID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if provider_type is not None: params['providerType'] = provider_type
        if document_provider_id is not None: params['documentProviderID'] = document_provider_id
        if document_provider_config_id is not None: params['documentProviderConfigID'] = document_provider_config_id
        data = self.session.put(self.api_url()+'/getAuthenticationUrlForProvider', params)
        return data['result']

    def get_thumbnail_path(self, provider_type=None, provider_id=None, last_modified_date=None, id=None):
        """
        The ``getThumbnailPath`` action.
        
        :param provider_type: providerType (type: ``string``)
        :param provider_id: providerID (type: ``string``)
        :param last_modified_date: lastModifiedDate (type: ``string``)
        :param id: id (type: ``string``)
        :return: ``string``
        """
        params = {}
        if provider_type is not None: params['providerType'] = provider_type
        if provider_id is not None: params['providerID'] = provider_id
        if last_modified_date is not None: params['lastModifiedDate'] = last_modified_date
        if id is not None: params['id'] = id
        data = self.session.put(self.api_url()+'/getThumbnailPath', params)
        return data['result']

    def load_external_browse_location(self, provider_type=None, document_provider_id=None, link_action=None):
        """
        The ``loadExternalBrowseLocation`` action.
        
        :param provider_type: providerType (type: ``string``)
        :param document_provider_id: documentProviderID (type: ``string``)
        :param link_action: linkAction (type: ``string``)
        :return: ``string[]``
        """
        params = {}
        if provider_type is not None: params['providerType'] = provider_type
        if document_provider_id is not None: params['documentProviderID'] = document_provider_id
        if link_action is not None: params['linkAction'] = link_action
        data = self.session.put(self.api_url()+'/loadExternalBrowseLocation', params)
        return data['result']

    def save_external_browse_location(self, provider_type=None, document_provider_id=None, link_action=None, breadcrumb=None):
        """
        The ``saveExternalBrowseLocation`` action.
        
        :param provider_type: providerType (type: ``string``)
        :param document_provider_id: documentProviderID (type: ``string``)
        :param link_action: linkAction (type: ``string``)
        :param breadcrumb: breadcrumb (type: ``string``)
        """
        params = {}
        if provider_type is not None: params['providerType'] = provider_type
        if document_provider_id is not None: params['documentProviderID'] = document_provider_id
        if link_action is not None: params['linkAction'] = link_action
        if breadcrumb is not None: params['breadcrumb'] = breadcrumb
        data = self.session.put(self.api_url()+'/saveExternalBrowseLocation', params)
        

    def show_external_thumbnails(self):
        """
        The ``showExternalThumbnails`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/showExternalThumbnails', params)
        return data['result']

api.register(ExternalDocument)


class ExternalSection(Object):
    code = 'EXTSEC'
    app_global_id = Field('appGlobalID')
    calculated_url = Field('calculatedURL')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    frame = Field('frame')
    friendly_url = Field('friendlyURL')
    global_uikey = Field('globalUIKey')
    height = Field('height')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_interface = Field('objInterface')
    obj_obj_code = Field('objObjCode')
    scrolling = Field('scrolling')
    url = Field('url')
    view_id = Field('viewID')
    app_global = Reference('appGlobal')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    view = Reference('view')

    def calculate_url(self, external_section_id=None, obj_code=None, obj_id=None):
        """
        The ``calculateURL`` action.
        
        :param external_section_id: externalSectionID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if external_section_id is not None: params['externalSectionID'] = external_section_id
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/calculateURL', params)
        return data['result']

    def calculate_urls(self, external_section_ids=None, obj_code=None, obj_id=None):
        """
        The ``calculateURLS`` action.
        
        :param external_section_ids: externalSectionIDs (type: ``java.util.Collection``)
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :return: ``map``
        """
        params = {}
        if external_section_ids is not None: params['externalSectionIDs'] = external_section_ids
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/calculateURLS', params)
        return data['result']

api.register(ExternalSection)


class Favorite(Object):
    code = 'FVRITE'
    customer_id = Field('customerID')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    user_id = Field('userID')
    customer = Reference('customer')
    user = Reference('user')

    def update_favorite_name(self, name=None, favorite_id=None):
        """
        The ``updateFavoriteName`` action.
        
        :param name: name (type: ``string``)
        :param favorite_id: favoriteID (type: ``string``)
        """
        params = {}
        if name is not None: params['name'] = name
        if favorite_id is not None: params['favoriteID'] = favorite_id
        data = self.session.put(self.api_url()+'/updateFavoriteName', params)
        

api.register(Favorite)


class Feature(Object):
    code = 'FEATR'
    app_global_id = Field('appGlobalID')
    jexl_expression = Field('jexlExpression')
    jexl_updated_date = Field('jexlUpdatedDate')
    name = Field('name')
    old_jexl_expression = Field('oldJexlExpression')
    app_global = Reference('appGlobal')

    def export(self):
        """
        The ``export`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/export', params)
        return data['result']

    def is_enabled(self, name=None):
        """
        The ``isEnabled`` action.
        
        :param name: name (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if name is not None: params['name'] = name
        data = self.session.put(self.api_url()+'/isEnabled', params)
        return data['result']

    def override_for_session(self, name=None, value=None):
        """
        The ``overrideForSession`` action.
        
        :param name: name (type: ``string``)
        :param value: value (type: ``boolean``)
        """
        params = {}
        if name is not None: params['name'] = name
        if value is not None: params['value'] = value
        data = self.session.put(self.api_url()+'/overrideForSession', params)
        

api.register(Feature)


class FinancialData(Object):
    code = 'FINDAT'
    actual_expense_cost = Field('actualExpenseCost')
    actual_fixed_revenue = Field('actualFixedRevenue')
    actual_labor_cost = Field('actualLaborCost')
    actual_labor_cost_hours = Field('actualLaborCostHours')
    actual_labor_revenue = Field('actualLaborRevenue')
    allocationdate = Field('allocationdate')
    customer_id = Field('customerID')
    fixed_cost = Field('fixedCost')
    is_split = Field('isSplit')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_fixed_revenue = Field('plannedFixedRevenue')
    planned_labor_cost = Field('plannedLaborCost')
    planned_labor_cost_hours = Field('plannedLaborCostHours')
    planned_labor_revenue = Field('plannedLaborRevenue')
    project_id = Field('projectID')
    total_actual_cost = Field('totalActualCost')
    total_actual_revenue = Field('totalActualRevenue')
    total_planned_cost = Field('totalPlannedCost')
    total_planned_revenue = Field('totalPlannedRevenue')
    total_variance_cost = Field('totalVarianceCost')
    total_variance_revenue = Field('totalVarianceRevenue')
    variance_expense_cost = Field('varianceExpenseCost')
    variance_labor_cost = Field('varianceLaborCost')
    variance_labor_cost_hours = Field('varianceLaborCostHours')
    variance_labor_revenue = Field('varianceLaborRevenue')
    customer = Reference('customer')
    project = Reference('project')

api.register(FinancialData)


class Group(Object):
    code = 'GROUP'
    customer_id = Field('customerID')
    default_interface = Field('defaultInterface')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    parent_id = Field('parentID')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    parent = Reference('parent')
    children = Collection('children')
    user_groups = Collection('userGroups')

    def add_early_access(self, ids=None):
        """
        The ``addEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/addEarlyAccess', params)
        

    def check_delete(self, ids=None):
        """
        The ``checkDelete`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/checkDelete', params)
        

    def delete_early_access(self, ids=None):
        """
        The ``deleteEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/deleteEarlyAccess', params)
        

    def has_reference(self, ids=None):
        """
        The ``hasReference`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/hasReference', params)
        return data['result']

    def replace_delete_groups(self, ids=None, replace_group_id=None):
        """
        The ``replaceDeleteGroups`` action.
        
        :param ids: ids (type: ``string[]``)
        :param replace_group_id: replaceGroupID (type: ``string``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        if replace_group_id is not None: params['replaceGroupID'] = replace_group_id
        data = self.session.put(self.api_url()+'/replaceDeleteGroups', params)
        

api.register(Group)


class Hour(Object):
    code = 'HOUR'
    accessor_ids = Field('accessorIDs')
    actual_cost = Field('actualCost')
    approved_by_id = Field('approvedByID')
    approved_on_date = Field('approvedOnDate')
    billing_record_id = Field('billingRecordID')
    customer_id = Field('customerID')
    description = Field('description')
    dup_id = Field('dupID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_rate_override = Field('hasRateOverride')
    hour_type_id = Field('hourTypeID')
    hours = Field('hours')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    op_task_id = Field('opTaskID')
    owner_id = Field('ownerID')
    project_id = Field('projectID')
    project_overhead_id = Field('projectOverheadID')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    resource_revenue = Field('resourceRevenue')
    role_id = Field('roleID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    status = Field('status')
    task_id = Field('taskID')
    timesheet_id = Field('timesheetID')
    approved_by = Reference('approvedBy')
    billing_record = Reference('billingRecord')
    customer = Reference('customer')
    hour_type = Reference('hourType')
    last_updated_by = Reference('lastUpdatedBy')
    op_task = Reference('opTask')
    owner = Reference('owner')
    project = Reference('project')
    project_overhead = Reference('projectOverhead')
    role = Reference('role')
    task = Reference('task')
    timesheet = Reference('timesheet')

    def approve(self):
        """
        The ``approve`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/approve', params)
        

    def unapprove(self):
        """
        The ``unapprove`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unapprove', params)
        

api.register(Hour)


class HourType(Object):
    code = 'HOURT'
    app_global_id = Field('appGlobalID')
    count_as_revenue = Field('countAsRevenue')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    display_obj_obj_code = Field('displayObjObjCode')
    ext_ref_id = Field('extRefID')
    is_active = Field('isActive')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    overhead_type = Field('overheadType')
    scope = Field('scope')
    app_global = Reference('appGlobal')
    customer = Reference('customer')
    timesheetprofiles = Collection('timesheetprofiles')
    users = Collection('users')

    def has_reference(self, ids=None):
        """
        The ``hasReference`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/hasReference', params)
        return data['result']

api.register(HourType)


class IPRange(Object):
    code = 'IPRAGE'
    customer_id = Field('customerID')
    end_range = Field('endRange')
    start_range = Field('startRange')
    customer = Reference('customer')

api.register(IPRange)


class ImportRow(Object):
    code = 'IROW'
    column_number = Field('columnNumber')
    customer_id = Field('customerID')
    field_name = Field('fieldName')
    import_template_id = Field('importTemplateID')
    customer = Reference('customer')
    import_template = Reference('importTemplate')

api.register(ImportRow)


class ImportTemplate(Object):
    code = 'ITMPL'
    begin_at_row = Field('beginAtRow')
    customer_id = Field('customerID')
    import_obj_code = Field('importObjCode')
    name = Field('name')
    customer = Reference('customer')
    import_rows = Collection('importRows')

api.register(ImportTemplate)


class InstalledDDItem(Object):
    code = 'IDDI'
    iddiobj_code = Field('IDDIObjCode')
    customer_id = Field('customerID')
    name_key = Field('nameKey')
    customer = Reference('customer')

api.register(InstalledDDItem)


class Issue(Object):
    code = 'OPTASK'
    accessor_ids = Field('accessorIDs')
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_start_date = Field('actualStartDate')
    actual_work_required = Field('actualWorkRequired')
    actual_work_required_expression = Field('actualWorkRequiredExpression')
    age_range_as_string = Field('ageRangeAsString')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    assigned_to_id = Field('assignedToID')
    audit_types = Field('auditTypes')
    auto_closure_date = Field('autoClosureDate')
    can_start = Field('canStart')
    category_id = Field('categoryID')
    commit_date = Field('commitDate')
    commit_date_range = Field('commitDateRange')
    condition = Field('condition')
    current_approval_step_id = Field('currentApprovalStepID')
    current_status_duration = Field('currentStatusDuration')
    customer_id = Field('customerID')
    description = Field('description')
    display_queue_breadcrumb = Field('displayQueueBreadcrumb')
    due_date = Field('dueDate')
    duration_minutes = Field('durationMinutes')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    first_response = Field('firstResponse')
    has_documents = Field('hasDocuments')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_resolvables = Field('hasResolvables')
    has_timed_notifications = Field('hasTimedNotifications')
    how_old = Field('howOld')
    is_complete = Field('isComplete')
    is_help_desk = Field('isHelpDesk')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    number_of_children = Field('numberOfChildren')
    olv = Field('olv')
    op_task_type = Field('opTaskType')
    op_task_type_label = Field('opTaskTypeLabel')
    owner_id = Field('ownerID')
    planned_completion_date = Field('plannedCompletionDate')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_duration_minutes = Field('plannedDurationMinutes')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_start_date = Field('plannedStartDate')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    project_id = Field('projectID')
    projected_completion_date = Field('projectedCompletionDate')
    projected_duration_minutes = Field('projectedDurationMinutes')
    projected_start_date = Field('projectedStartDate')
    queue_topic_breadcrumb = Field('queueTopicBreadcrumb')
    queue_topic_id = Field('queueTopicID')
    reference_number = Field('referenceNumber')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_duration_minutes = Field('remainingDurationMinutes')
    resolution_time = Field('resolutionTime')
    resolve_op_task_id = Field('resolveOpTaskID')
    resolve_project_id = Field('resolveProjectID')
    resolve_task_id = Field('resolveTaskID')
    resolving_obj_code = Field('resolvingObjCode')
    resolving_obj_id = Field('resolvingObjID')
    role_id = Field('roleID')
    security_ancestors_disabled = Field('securityAncestorsDisabled')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    severity = Field('severity')
    show_commit_date = Field('showCommitDate')
    show_condition = Field('showCondition')
    show_status = Field('showStatus')
    source_obj_code = Field('sourceObjCode')
    source_obj_id = Field('sourceObjID')
    source_task_id = Field('sourceTaskID')
    status = Field('status')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    team_id = Field('teamID')
    url = Field('url')
    version = Field('version')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    category = Reference('category')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    owner = Reference('owner')
    parent = Reference('parent')
    primary_assignment = Reference('primaryAssignment')
    project = Reference('project')
    queue_topic = Reference('queueTopic')
    rejection_issue = Reference('rejectionIssue')
    resolve_op_task = Reference('resolveOpTask')
    resolve_project = Reference('resolveProject')
    resolve_task = Reference('resolveTask')
    role = Reference('role')
    source_task = Reference('sourceTask')
    submitted_by = Reference('submittedBy')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    work_item = Reference('workItem')
    access_rules = Collection('accessRules')
    all_priorities = Collection('allPriorities')
    all_severities = Collection('allSeverities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    assignments = Collection('assignments')
    awaiting_approvals = Collection('awaitingApprovals')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    done_statuses = Collection('doneStatuses')
    hours = Collection('hours')
    notification_records = Collection('notificationRecords')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')
    resolvables = Collection('resolvables')
    security_ancestors = Collection('securityAncestors')
    updates = Collection('updates')

    def accept_work(self):
        """
        The ``acceptWork`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/acceptWork', params)
        

    def approve_approval(self, user_id=None, username=None, password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``approveApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/approveApproval', params)
        

    def assign(self, obj_id=None, obj_code=None):
        """
        The ``assign`` action.
        
        :param obj_id: objID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if obj_code is not None: params['objCode'] = obj_code
        data = self.session.put(self.api_url()+'/assign', params)
        

    def assign_multiple(self, user_ids=None, role_ids=None, team_id=None):
        """
        The ``assignMultiple`` action.
        
        :param user_ids: userIDs (type: ``string[]``)
        :param role_ids: roleIDs (type: ``string[]``)
        :param team_id: teamID (type: ``string``)
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        if role_ids is not None: params['roleIDs'] = role_ids
        if team_id is not None: params['teamID'] = team_id
        data = self.session.put(self.api_url()+'/assignMultiple', params)
        

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def convert_to_project(self, project=None, exchange_rate=None, options=None):
        """
        The ``convertToProject`` action.
        
        :param project: project (type: ``Project``)
        :param exchange_rate: exchangeRate (type: ``ExchangeRate``)
        :param options: options (type: ``string[]``)
        :return: ``string``
        """
        params = {}
        if project is not None: params['project'] = project
        if exchange_rate is not None: params['exchangeRate'] = exchange_rate
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/convertToProject', params)
        return data['result']

    def mark_done(self, status=None):
        """
        The ``markDone`` action.
        
        :param status: status (type: ``string``)
        """
        params = {}
        if status is not None: params['status'] = status
        data = self.session.put(self.api_url()+'/markDone', params)
        

    def mark_not_done(self, assignment_id=None):
        """
        The ``markNotDone`` action.
        
        :param assignment_id: assignmentID (type: ``string``)
        """
        params = {}
        if assignment_id is not None: params['assignmentID'] = assignment_id
        data = self.session.put(self.api_url()+'/markNotDone', params)
        

    def move(self, project_id=None):
        """
        The ``move`` action.
        
        :param project_id: projectID (type: ``string``)
        """
        params = {}
        if project_id is not None: params['projectID'] = project_id
        data = self.session.put(self.api_url()+'/move', params)
        

    def move_to_task(self, project_id=None, parent_id=None):
        """
        The ``moveToTask`` action.
        
        :param project_id: projectID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        """
        params = {}
        if project_id is not None: params['projectID'] = project_id
        if parent_id is not None: params['parentID'] = parent_id
        data = self.session.put(self.api_url()+'/moveToTask', params)
        

    def recall_approval(self):
        """
        The ``recallApproval`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/recallApproval', params)
        

    def reject_approval(self, user_id=None, username=None, password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``rejectApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/rejectApproval', params)
        

    def reply_to_assignment(self, note_text=None, commit_date=None):
        """
        The ``replyToAssignment`` action.
        
        :param note_text: noteText (type: ``string``)
        :param commit_date: commitDate (type: ``dateTime``)
        """
        params = {}
        if note_text is not None: params['noteText'] = note_text
        if commit_date is not None: params['commitDate'] = commit_date
        data = self.session.put(self.api_url()+'/replyToAssignment', params)
        

    def timed_notifications(self, notification_ids=None):
        """
        The ``timedNotifications`` action.
        
        :param notification_ids: notificationIDs (type: ``string[]``)
        """
        params = {}
        if notification_ids is not None: params['notificationIDs'] = notification_ids
        data = self.session.put(self.api_url()+'/timedNotifications', params)
        

    def unaccept_work(self):
        """
        The ``unacceptWork`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unacceptWork', params)
        

    def unassign(self, user_id=None):
        """
        The ``unassign`` action.
        
        :param user_id: userID (type: ``string``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/unassign', params)
        

    def add_comment(self, text):
        """
        Add a comment to the current object containing the supplied text.

        The new :class:`Comment` instance is returned, it does not need to be
        saved.
        """

        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.code,
            obj_id = self.id
        )
        comment.save()
        return comment

    def convert_to_task(self):
        """
        Convert this issue to a task.
        The newly converted task will be returned, it does not need to be
        saved.
        """
        data = self.session.put(
            self.api_url()+'/convertToTask',
            params=dict(
                updates=dict(
                    options=['preserveIssue',
                             'preservePrimaryContact',
                             'preserveUpdates'],
                    task=dict(name=self.name,
                              description=self.description,
                              enteredByID=self.entered_by_id,
                              )
            )))
        return self.session.api.Task(self.session, ID=data['result'])

api.register(Issue)


class Iteration(Object):
    code = 'ITRN'
    url = Field('URL')
    capacity = Field('capacity')
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    end_date = Field('endDate')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    estimate_completed = Field('estimateCompleted')
    focus_factor = Field('focusFactor')
    goal = Field('goal')
    has_documents = Field('hasDocuments')
    has_notes = Field('hasNotes')
    is_legacy = Field('isLegacy')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    original_total_estimate = Field('originalTotalEstimate')
    owner_id = Field('ownerID')
    percent_complete = Field('percentComplete')
    start_date = Field('startDate')
    status = Field('status')
    target_percent_complete = Field('targetPercentComplete')
    task_ids = Field('taskIDs')
    team_id = Field('teamID')
    total_estimate = Field('totalEstimate')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    owner = Reference('owner')
    team = Reference('team')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')

    def assign_iteration_to_descendants(self, task_ids=None, iteration_id=None):
        """
        The ``assignIterationToDescendants`` action.
        
        :param task_ids: taskIDs (type: ``string[]``)
        :param iteration_id: iterationID (type: ``string``)
        """
        params = {}
        if task_ids is not None: params['taskIDs'] = task_ids
        if iteration_id is not None: params['iterationID'] = iteration_id
        data = self.session.put(self.api_url()+'/assignIterationToDescendants', params)
        

    def legacy_burndown_info_with_percentage(self, iteration_id=None):
        """
        The ``legacyBurndownInfoWithPercentage`` action.
        
        :param iteration_id: iterationID (type: ``string``)
        :return: ``map``
        """
        params = {}
        if iteration_id is not None: params['iterationID'] = iteration_id
        data = self.session.put(self.api_url()+'/legacyBurndownInfoWithPercentage', params)
        return data['result']

    def legacy_burndown_info_with_points(self, iteration_id=None):
        """
        The ``legacyBurndownInfoWithPoints`` action.
        
        :param iteration_id: iterationID (type: ``string``)
        :return: ``map``
        """
        params = {}
        if iteration_id is not None: params['iterationID'] = iteration_id
        data = self.session.put(self.api_url()+'/legacyBurndownInfoWithPoints', params)
        return data['result']

api.register(Iteration)


class JournalEntry(Object):
    code = 'JRNLE'
    accessor_ids = Field('accessorIDs')
    approver_status_id = Field('approverStatusID')
    assignment_id = Field('assignmentID')
    audit_record_id = Field('auditRecordID')
    aux1 = Field('aux1')
    aux2 = Field('aux2')
    aux3 = Field('aux3')
    baseline_id = Field('baselineID')
    billing_record_id = Field('billingRecordID')
    change_type = Field('changeType')
    customer_id = Field('customerID')
    document_approval_id = Field('documentApprovalID')
    document_id = Field('documentID')
    document_share_id = Field('documentShareID')
    duration_minutes = Field('durationMinutes')
    edited_by_id = Field('editedByID')
    entry_date = Field('entryDate')
    expense_id = Field('expenseID')
    ext_ref_id = Field('extRefID')
    field_name = Field('fieldName')
    flags = Field('flags')
    hour_id = Field('hourID')
    new_date_val = Field('newDateVal')
    new_number_val = Field('newNumberVal')
    new_text_val = Field('newTextVal')
    num_likes = Field('numLikes')
    num_replies = Field('numReplies')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    old_date_val = Field('oldDateVal')
    old_number_val = Field('oldNumberVal')
    old_text_val = Field('oldTextVal')
    op_task_id = Field('opTaskID')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    reference_object_name = Field('referenceObjectName')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    sub_obj_code = Field('subObjCode')
    sub_obj_id = Field('subObjID')
    sub_reference_object_name = Field('subReferenceObjectName')
    task_id = Field('taskID')
    template_id = Field('templateID')
    timesheet_id = Field('timesheetID')
    top_obj_code = Field('topObjCode')
    top_obj_id = Field('topObjID')
    top_reference_object_name = Field('topReferenceObjectName')
    user_id = Field('userID')
    approver_status = Reference('approverStatus')
    assignment = Reference('assignment')
    audit_record = Reference('auditRecord')
    baseline = Reference('baseline')
    billing_record = Reference('billingRecord')
    customer = Reference('customer')
    document = Reference('document')
    document_approval = Reference('documentApproval')
    document_share = Reference('documentShare')
    edited_by = Reference('editedBy')
    expense = Reference('expense')
    hour = Reference('hour')
    op_task = Reference('opTask')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    timesheet = Reference('timesheet')
    user = Reference('user')
    replies = Collection('replies')

    def edit_field_names(self, parameter_id=None, field_name=None):
        """
        The ``editFieldNames`` action.
        
        :param parameter_id: parameterID (type: ``string``)
        :param field_name: fieldName (type: ``string``)
        :return: ``string[]``
        """
        params = {}
        if parameter_id is not None: params['parameterID'] = parameter_id
        if field_name is not None: params['fieldName'] = field_name
        data = self.session.put(self.api_url()+'/editFieldNames', params)
        return data['result']

    def get_liked_journal_entry_ids(self, journal_entry_ids=None):
        """
        The ``getLikedJournalEntryIDs`` action.
        
        :param journal_entry_ids: journalEntryIDs (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if journal_entry_ids is not None: params['journalEntryIDs'] = journal_entry_ids
        data = self.session.put(self.api_url()+'/getLikedJournalEntryIDs', params)
        return data['result']

    def like(self):
        """
        The ``like`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/like', params)
        

    def unlike(self):
        """
        The ``unlike`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unlike', params)
        

api.register(JournalEntry)


class JournalField(Object):
    code = 'JRNLF'
    action = Field('action')
    customer_id = Field('customerID')
    display_name = Field('displayName')
    ext_ref_id = Field('extRefID')
    field_name = Field('fieldName')
    is_duration_enabled = Field('isDurationEnabled')
    obj_obj_code = Field('objObjCode')
    parameter_id = Field('parameterID')
    customer = Reference('customer')
    parameter = Reference('parameter')

    def migrate_wild_card_journal_fields(self):
        """
        The ``migrateWildCardJournalFields`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/migrateWildCardJournalFields', params)
        

    def set_journal_fields_for_obj_code(self, obj_code=None, messages=None):
        """
        The ``setJournalFieldsForObjCode`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param messages: messages (type: ``com.attask.model.RKJournalField[]``)
        :return: ``string[]``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if messages is not None: params['messages'] = messages
        data = self.session.put(self.api_url()+'/setJournalFieldsForObjCode', params)
        return data['result']

api.register(JournalField)


class KickStart(Object):
    code = 'KSS'
    obj_code = Field('objCode')

    def import_kick_start(self, file_handle=None, file_type=None):
        """
        The ``importKickStart`` action.
        
        :param file_handle: fileHandle (type: ``string``)
        :param file_type: fileType (type: ``string``)
        :return: ``map``
        """
        params = {}
        if file_handle is not None: params['fileHandle'] = file_handle
        if file_type is not None: params['fileType'] = file_type
        data = self.session.put(self.api_url()+'/importKickStart', params)
        return data['result']

api.register(KickStart)


class LayoutTemplate(Object):
    code = 'LYTMPL'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    default_nav_item = Field('defaultNavItem')
    description = Field('description')
    description_key = Field('descriptionKey')
    ext_ref_id = Field('extRefID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    license_type = Field('licenseType')
    name = Field('name')
    name_key = Field('nameKey')
    nav_bar = Field('navBar')
    nav_items = Field('navItems')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    app_global = Reference('appGlobal')
    customer = Reference('customer')
    last_updated_by = Reference('lastUpdatedBy')
    layout_template_cards = Collection('layoutTemplateCards')
    layout_template_date_preferences = Collection('layoutTemplateDatePreferences')
    layout_template_pages = Collection('layoutTemplatePages')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')
    ui_filters = Collection('uiFilters')
    ui_group_bys = Collection('uiGroupBys')
    ui_views = Collection('uiViews')

    def clear_all_custom_tabs(self, reset_default_nav=None, reset_nav_items=None):
        """
        The ``clearAllCustomTabs`` action.
        
        :param reset_default_nav: resetDefaultNav (type: ``boolean``)
        :param reset_nav_items: resetNavItems (type: ``boolean``)
        """
        params = {}
        if reset_default_nav is not None: params['resetDefaultNav'] = reset_default_nav
        if reset_nav_items is not None: params['resetNavItems'] = reset_nav_items
        data = self.session.put(self.api_url()+'/clearAllCustomTabs', params)
        

    def clear_all_user_custom_tabs(self, user_ids=None, reset_default_nav=None, reset_nav_items=None):
        """
        The ``clearAllUserCustomTabs`` action.
        
        :param user_ids: userIDs (type: ``java.util.Set``)
        :param reset_default_nav: resetDefaultNav (type: ``boolean``)
        :param reset_nav_items: resetNavItems (type: ``boolean``)
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        if reset_default_nav is not None: params['resetDefaultNav'] = reset_default_nav
        if reset_nav_items is not None: params['resetNavItems'] = reset_nav_items
        data = self.session.put(self.api_url()+'/clearAllUserCustomTabs', params)
        

    def clear_ppmigration_flag(self):
        """
        The ``clearPPMigrationFlag`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/clearPPMigrationFlag', params)
        

    def clear_user_custom_tabs(self, user_ids=None, reset_default_nav=None, reset_nav_items=None, layout_page_types=None):
        """
        The ``clearUserCustomTabs`` action.
        
        :param user_ids: userIDs (type: ``java.util.Set``)
        :param reset_default_nav: resetDefaultNav (type: ``boolean``)
        :param reset_nav_items: resetNavItems (type: ``boolean``)
        :param layout_page_types: layoutPageTypes (type: ``java.util.Set``)
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        if reset_default_nav is not None: params['resetDefaultNav'] = reset_default_nav
        if reset_nav_items is not None: params['resetNavItems'] = reset_nav_items
        if layout_page_types is not None: params['layoutPageTypes'] = layout_page_types
        data = self.session.put(self.api_url()+'/clearUserCustomTabs', params)
        

    def get_layout_template_cards_by_card_location(self, layout_template_id=None, card_location=None):
        """
        The ``getLayoutTemplateCardsByCardLocation`` action.
        
        :param layout_template_id: layoutTemplateID (type: ``string``)
        :param card_location: cardLocation (type: ``string``)
        :return: ``string[]``
        """
        params = {}
        if layout_template_id is not None: params['layoutTemplateID'] = layout_template_id
        if card_location is not None: params['cardLocation'] = card_location
        data = self.session.put(self.api_url()+'/getLayoutTemplateCardsByCardLocation', params)
        return data['result']

    def get_layout_template_users(self, layout_template_ids=None):
        """
        The ``getLayoutTemplateUsers`` action.
        
        :param layout_template_ids: layoutTemplateIDs (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if layout_template_ids is not None: params['layoutTemplateIDs'] = layout_template_ids
        data = self.session.put(self.api_url()+'/getLayoutTemplateUsers', params)
        return data['result']

    def migrate_portal_profile(self, portal_profile_ids=None):
        """
        The ``migratePortalProfile`` action.
        
        :param portal_profile_ids: portalProfileIDs (type: ``string[]``)
        :return: ``map``
        """
        params = {}
        if portal_profile_ids is not None: params['portalProfileIDs'] = portal_profile_ids
        data = self.session.put(self.api_url()+'/migratePortalProfile', params)
        return data['result']

api.register(LayoutTemplate)


class LayoutTemplateCard(Object):
    code = 'LTMPLC'
    card_location = Field('cardLocation')
    card_type = Field('cardType')
    custom_label = Field('customLabel')
    customer_id = Field('customerID')
    data_type = Field('dataType')
    display_order = Field('displayOrder')
    field_name = Field('fieldName')
    group_name = Field('groupName')
    layout_template_id = Field('layoutTemplateID')
    parameter_id = Field('parameterID')
    customer = Reference('customer')
    layout_template = Reference('layoutTemplate')

api.register(LayoutTemplateCard)


class LayoutTemplateDatePreference(Object):
    code = 'LTMPDP'
    card_location = Field('cardLocation')
    card_type = Field('cardType')
    customer_id = Field('customerID')
    date_preference = Field('datePreference')
    layout_template_id = Field('layoutTemplateID')
    customer = Reference('customer')
    layout_template = Reference('layoutTemplate')

api.register(LayoutTemplateDatePreference)


class LayoutTemplatePage(Object):
    code = 'LTMPLP'
    customer_id = Field('customerID')
    layout_template_id = Field('layoutTemplateID')
    page_type = Field('pageType')
    tabs = Field('tabs')
    customer = Reference('customer')
    layout_template = Reference('layoutTemplate')

api.register(LayoutTemplatePage)


class LicenseOrder(Object):
    code = 'LICEOR'
    customer_id = Field('customerID')
    description = Field('description')
    exp_date = Field('expDate')
    ext_ref_id = Field('extRefID')
    external_users_enabled = Field('externalUsersEnabled')
    full_users = Field('fullUsers')
    is_apienabled = Field('isAPIEnabled')
    is_enterprise = Field('isEnterprise')
    is_soapenabled = Field('isSOAPEnabled')
    limited_users = Field('limitedUsers')
    order_date = Field('orderDate')
    requestor_users = Field('requestorUsers')
    review_users = Field('reviewUsers')
    team_users = Field('teamUsers')
    customer = Reference('customer')

api.register(LicenseOrder)


class Like(Object):
    code = 'LIKE'
    customer_id = Field('customerID')
    endorsement_id = Field('endorsementID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    journal_entry_id = Field('journalEntryID')
    note_id = Field('noteID')
    customer = Reference('customer')
    endorsement = Reference('endorsement')
    entered_by = Reference('enteredBy')
    journal_entry = Reference('journalEntry')
    note = Reference('note')

api.register(Like)


class LinkedFolder(Object):
    code = 'LNKFDR'
    customer_id = Field('customerID')
    document_provider_id = Field('documentProviderID')
    external_integration_type = Field('externalIntegrationType')
    external_storage_id = Field('externalStorageID')
    folder_id = Field('folderID')
    is_top_level_folder = Field('isTopLevelFolder')
    last_sync_date = Field('lastSyncDate')
    linked_by_id = Field('linkedByID')
    linked_date = Field('linkedDate')
    customer = Reference('customer')
    document_provider = Reference('documentProvider')
    folder = Reference('folder')
    linked_by = Reference('linkedBy')

api.register(LinkedFolder)


class MasterTask(Object):
    code = 'MTSK'
    url = Field('URL')
    assigned_to_id = Field('assignedToID')
    audit_types = Field('auditTypes')
    billing_amount = Field('billingAmount')
    category_id = Field('categoryID')
    cost_amount = Field('costAmount')
    cost_type = Field('costType')
    customer_id = Field('customerID')
    description = Field('description')
    duration_minutes = Field('durationMinutes')
    duration_type = Field('durationType')
    duration_unit = Field('durationUnit')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    is_duration_locked = Field('isDurationLocked')
    is_work_required_locked = Field('isWorkRequiredLocked')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    milestone_id = Field('milestoneID')
    name = Field('name')
    planned_cost = Field('plannedCost')
    planned_revenue = Field('plannedRevenue')
    priority = Field('priority')
    revenue_type = Field('revenueType')
    role_id = Field('roleID')
    team_id = Field('teamID')
    tracking_mode = Field('trackingMode')
    work_required = Field('workRequired')
    assigned_to = Reference('assignedTo')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    milestone = Reference('milestone')
    role = Reference('role')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    assignments = Collection('assignments')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    expenses = Collection('expenses')
    groups = Collection('groups')
    notification_records = Collection('notificationRecords')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

api.register(MasterTask)


class MessageArg(Object):
    code = 'MSGARG'
    allowed_actions = Field('allowedActions')
    color = Field('color')
    href = Field('href')
    objcode = Field('objcode')
    objid = Field('objid')
    text = Field('text')
    type = Field('type')

api.register(MessageArg)


class MetaRecord(Object):
    code = 'PRSTOBJ'
    actions = Field('actions')
    bean_classname = Field('beanClassname')
    classname = Field('classname')
    common_display_order = Field('commonDisplayOrder')
    external_actions = Field('externalActions')
    is_asp = Field('isASP')
    is_common = Field('isCommon')
    limit_non_view_external = Field('limitNonViewExternal')
    limit_non_view_hd = Field('limitNonViewHD')
    limit_non_view_review = Field('limitNonViewReview')
    limit_non_view_ts = Field('limitNonViewTS')
    limit_non_view_team = Field('limitNonViewTeam')
    limited_actions = Field('limitedActions')
    message_key = Field('messageKey')
    obj_code = Field('objCode')
    pk_field_name = Field('pkFieldName')
    pk_table_name = Field('pkTableName')
    requestor_actions = Field('requestorActions')
    review_actions = Field('reviewActions')
    team_actions = Field('teamActions')

api.register(MetaRecord)


class Milestone(Object):
    code = 'MILE'
    color = Field('color')
    customer_id = Field('customerID')
    description = Field('description')
    ext_ref_id = Field('extRefID')
    milestone_path_id = Field('milestonePathID')
    name = Field('name')
    sequence = Field('sequence')
    customer = Reference('customer')
    milestone_path = Reference('milestonePath')

api.register(Milestone)


class MilestonePath(Object):
    code = 'MPATH'
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    groups = Collection('groups')
    milestones = Collection('milestones')

api.register(MilestonePath)


class MobileDevice(Object):
    code = 'MOBILDVC'
    device_token = Field('deviceToken')
    device_type = Field('deviceType')
    endpoint = Field('endpoint')
    user = Reference('user')

api.register(MobileDevice)


class NonWorkDay(Object):
    code = 'NONWKD'
    customer_id = Field('customerID')
    non_work_date = Field('nonWorkDate')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    schedule_day = Field('scheduleDay')
    schedule_id = Field('scheduleID')
    user_id = Field('userID')
    customer = Reference('customer')
    schedule = Reference('schedule')
    user = Reference('user')

api.register(NonWorkDay)


class Note(Object):
    code = 'NOTE'
    accessor_ids = Field('accessorIDs')
    attach_document_id = Field('attachDocumentID')
    attach_obj_code = Field('attachObjCode')
    attach_obj_id = Field('attachObjID')
    attach_op_task_id = Field('attachOpTaskID')
    attach_work_id = Field('attachWorkID')
    attach_work_name = Field('attachWorkName')
    attach_work_obj_code = Field('attachWorkObjCode')
    attach_work_user_id = Field('attachWorkUserID')
    audit_record_id = Field('auditRecordID')
    audit_text = Field('auditText')
    audit_type = Field('auditType')
    customer_id = Field('customerID')
    document_id = Field('documentID')
    email_users = Field('emailUsers')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    format_entry_date = Field('formatEntryDate')
    has_replies = Field('hasReplies')
    indent = Field('indent')
    is_deleted = Field('isDeleted')
    is_message = Field('isMessage')
    is_private = Field('isPrivate')
    is_reply = Field('isReply')
    iteration_id = Field('iterationID')
    note_obj_code = Field('noteObjCode')
    note_text = Field('noteText')
    num_likes = Field('numLikes')
    num_replies = Field('numReplies')
    obj_id = Field('objID')
    op_task_id = Field('opTaskID')
    owner_id = Field('ownerID')
    parent_endorsement_id = Field('parentEndorsementID')
    parent_journal_entry_id = Field('parentJournalEntryID')
    parent_note_id = Field('parentNoteID')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    reference_object_name = Field('referenceObjectName')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    subject = Field('subject')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    thread_date = Field('threadDate')
    thread_id = Field('threadID')
    timesheet_id = Field('timesheetID')
    top_note_obj_code = Field('topNoteObjCode')
    top_obj_id = Field('topObjID')
    top_reference_object_name = Field('topReferenceObjectName')
    user_id = Field('userID')
    attach_document = Reference('attachDocument')
    attach_op_task = Reference('attachOpTask')
    attach_work_user = Reference('attachWorkUser')
    audit_record = Reference('auditRecord')
    customer = Reference('customer')
    document = Reference('document')
    iteration = Reference('iteration')
    op_task = Reference('opTask')
    owner = Reference('owner')
    parent_endorsement = Reference('parentEndorsement')
    parent_journal_entry = Reference('parentJournalEntry')
    parent_note = Reference('parentNote')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    timesheet = Reference('timesheet')
    user = Reference('user')
    replies = Collection('replies')
    tags = Collection('tags')

    def add_note_to_objects(self, obj_ids=None, note_obj_code=None, note_text=None, is_private=None, email_users=None, tags=None):
        """
        The ``addNoteToObjects`` action.
        
        :param obj_ids: objIDs (type: ``string[]``)
        :param note_obj_code: noteObjCode (type: ``string``)
        :param note_text: noteText (type: ``string``)
        :param is_private: isPrivate (type: ``boolean``)
        :param email_users: emailUsers (type: ``boolean``)
        :param tags: tags (type: ``java.lang.Object``)
        :return: ``string[]``
        """
        params = {}
        if obj_ids is not None: params['objIDs'] = obj_ids
        if note_obj_code is not None: params['noteObjCode'] = note_obj_code
        if note_text is not None: params['noteText'] = note_text
        if is_private is not None: params['isPrivate'] = is_private
        if email_users is not None: params['emailUsers'] = email_users
        if tags is not None: params['tags'] = tags
        data = self.session.put(self.api_url()+'/addNoteToObjects', params)
        return data['result']

    def get_liked_note_ids(self, note_ids=None):
        """
        The ``getLikedNoteIDs`` action.
        
        :param note_ids: noteIDs (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if note_ids is not None: params['noteIDs'] = note_ids
        data = self.session.put(self.api_url()+'/getLikedNoteIDs', params)
        return data['result']

    def like(self):
        """
        The ``like`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/like', params)
        

    def unlike(self):
        """
        The ``unlike`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unlike', params)
        

    def add_comment(self, text):
        """
        Add a comment to this comment.

        The new :class:`Comment` instance is returned, it does not need to be
        saved.
        """
        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.note_obj_code,
            obj_id = self.obj_id,
            parent_note_id=self.id
        )
        comment.save()
        return comment

api.register(Note)


class NoteTag(Object):
    code = 'NTAG'
    customer_id = Field('customerID')
    length = Field('length')
    note_id = Field('noteID')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    reference_object_name = Field('referenceObjectName')
    start_idx = Field('startIdx')
    team_id = Field('teamID')
    user_id = Field('userID')
    customer = Reference('customer')
    note = Reference('note')
    team = Reference('team')
    user = Reference('user')

api.register(NoteTag)


class NotificationRecord(Object):
    code = 'TMNR'
    customer_id = Field('customerID')
    email_sent_date = Field('emailSentDate')
    entry_date = Field('entryDate')
    master_task_id = Field('masterTaskID')
    notification_obj_code = Field('notificationObjCode')
    notification_obj_id = Field('notificationObjID')
    op_task_id = Field('opTaskID')
    project_id = Field('projectID')
    recipients = Field('recipients')
    scheduled_date = Field('scheduledDate')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    timed_notification_id = Field('timedNotificationID')
    timesheet_id = Field('timesheetID')
    timesheet_profile_id = Field('timesheetProfileID')
    customer = Reference('customer')
    master_task = Reference('masterTask')
    op_task = Reference('opTask')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    timed_notification = Reference('timedNotification')
    timesheet = Reference('timesheet')
    timesheet_profile = Reference('timesheetProfile')

api.register(NotificationRecord)


class ObjectCategory(Object):
    code = 'OBJCAT'
    category_id = Field('categoryID')
    category_order = Field('categoryOrder')
    customer_id = Field('customerID')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    category = Reference('category')
    customer = Reference('customer')

api.register(ObjectCategory)


class Parameter(Object):
    code = 'PARAM'
    customer_id = Field('customerID')
    data_type = Field('dataType')
    description = Field('description')
    display_size = Field('displaySize')
    display_type = Field('displayType')
    ext_ref_id = Field('extRefID')
    format_constraint = Field('formatConstraint')
    is_required = Field('isRequired')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    customer = Reference('customer')
    last_updated_by = Reference('lastUpdatedBy')
    parameter_options = Collection('parameterOptions')

api.register(Parameter)


class ParameterGroup(Object):
    code = 'PGRP'
    customer_id = Field('customerID')
    description = Field('description')
    display_order = Field('displayOrder')
    ext_ref_id = Field('extRefID')
    is_default = Field('isDefault')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    customer = Reference('customer')
    last_updated_by = Reference('lastUpdatedBy')

api.register(ParameterGroup)


class ParameterOption(Object):
    code = 'POPT'
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    ext_ref_id = Field('extRefID')
    is_default = Field('isDefault')
    is_hidden = Field('isHidden')
    label = Field('label')
    parameter_id = Field('parameterID')
    value = Field('value')
    customer = Reference('customer')
    parameter = Reference('parameter')

api.register(ParameterOption)


class ParameterValue(Object):
    code = 'PVAL'
    company_id = Field('companyID')
    customer_id = Field('customerID')
    date_val = Field('dateVal')
    document_id = Field('documentID')
    expense_id = Field('expenseID')
    interation_id = Field('interationID')
    master_task_id = Field('masterTaskID')
    number_val = Field('numberVal')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    op_task_id = Field('opTaskID')
    parameter_id = Field('parameterID')
    parameter_name = Field('parameterName')
    portfolio_id = Field('portfolioID')
    program_id = Field('programID')
    project_id = Field('projectID')
    task_id = Field('taskID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    text_val = Field('textVal')
    user_id = Field('userID')
    company = Reference('company')
    customer = Reference('customer')
    document = Reference('document')
    expense = Reference('expense')
    iteration = Reference('iteration')
    master_task = Reference('masterTask')
    op_task = Reference('opTask')
    parameter = Reference('parameter')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    task = Reference('task')
    template = Reference('template')
    template_task = Reference('templateTask')
    user = Reference('user')

api.register(ParameterValue)


class PopAccount(Object):
    code = 'POPA'
    customer_id = Field('customerID')
    entry_date = Field('entryDate')
    pop_disabled = Field('popDisabled')
    pop_enforce_ssl = Field('popEnforceSSL')
    pop_errors = Field('popErrors')
    pop_password = Field('popPassword')
    pop_port = Field('popPort')
    pop_server = Field('popServer')
    pop_user = Field('popUser')
    project_id = Field('projectID')
    customer = Reference('customer')
    project = Reference('project')

api.register(PopAccount)


class PortalProfile(Object):
    code = 'PTLPFL'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    description = Field('description')
    description_key = Field('descriptionKey')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    app_global = Reference('appGlobal')
    customer = Reference('customer')
    custom_menus = Collection('customMenus')
    custom_tabs = Collection('customTabs')
    portal_sections = Collection('portalSections')
    portal_tabs = Collection('portalTabs')
    ui_filters = Collection('uiFilters')
    ui_group_bys = Collection('uiGroupBys')
    ui_views = Collection('uiViews')

api.register(PortalProfile)


class PortalSection(Object):
    code = 'PTLSEC'
    accessor_ids = Field('accessorIDs')
    app_global_id = Field('appGlobalID')
    controller_class = Field('controllerClass')
    currency = Field('currency')
    customer_id = Field('customerID')
    default_tab = Field('defaultTab')
    definition = Field('definition')
    description = Field('description')
    description_key = Field('descriptionKey')
    enable_prompt_security = Field('enablePromptSecurity')
    entered_by_id = Field('enteredByID')
    ext_ref_id = Field('extRefID')
    filter_control = Field('filterControl')
    filter_id = Field('filterID')
    folder_name = Field('folderName')
    force_load = Field('forceLoad')
    global_uikey = Field('globalUIKey')
    group_by_id = Field('groupByID')
    group_control = Field('groupControl')
    is_app_global_copiable = Field('isAppGlobalCopiable')
    is_app_global_editable = Field('isAppGlobalEditable')
    is_new_format = Field('isNewFormat')
    is_public = Field('isPublic')
    is_report = Field('isReport')
    is_standalone = Field('isStandalone')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    max_results = Field('maxResults')
    method_name = Field('methodName')
    mod_date = Field('modDate')
    name = Field('name')
    name_key = Field('nameKey')
    obj_id = Field('objID')
    obj_interface = Field('objInterface')
    obj_obj_code = Field('objObjCode')
    preference_id = Field('preferenceID')
    public_run_as_user_id = Field('publicRunAsUserID')
    public_token = Field('publicToken')
    report_folder_id = Field('reportFolderID')
    report_type = Field('reportType')
    run_as_user_id = Field('runAsUserID')
    scheduled_report_id = Field('scheduledReportID')
    security_ancestors_disabled = Field('securityAncestorsDisabled')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    show_prompts = Field('showPrompts')
    sort_by = Field('sortBy')
    sort_by2 = Field('sortBy2')
    sort_by3 = Field('sortBy3')
    sort_type = Field('sortType')
    sort_type2 = Field('sortType2')
    sort_type3 = Field('sortType3')
    special_view = Field('specialView')
    tool_bar = Field('toolBar')
    ui_obj_code = Field('uiObjCode')
    view_control = Field('viewControl')
    view_id = Field('viewID')
    width = Field('width')
    app_global = Reference('appGlobal')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    filter = Reference('filter')
    group_by = Reference('groupBy')
    last_updated_by = Reference('lastUpdatedBy')
    preference = Reference('preference')
    public_run_as_user = Reference('publicRunAsUser')
    report_folder = Reference('reportFolder')
    run_as_user = Reference('runAsUser')
    scheduled_report = Reference('scheduledReport')
    view = Reference('view')
    access_rules = Collection('accessRules')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')
    portal_tab_sections = Collection('portalTabSections')
    scheduled_reports = Collection('scheduledReports')
    security_ancestors = Collection('securityAncestors')

    def get_pk(self, obj_code=None):
        """
        The ``getPK`` action.
        
        :param obj_code: objCode (type: ``string``)
        :return: ``string``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        data = self.session.put(self.api_url()+'/getPK', params)
        return data['result']

    def get_report_from_cache(self, background_job_id=None):
        """
        The ``getReportFromCache`` action.
        
        :param background_job_id: backgroundJobID (type: ``string``)
        :return: ``map``
        """
        params = {}
        if background_job_id is not None: params['backgroundJobID'] = background_job_id
        data = self.session.put(self.api_url()+'/getReportFromCache', params)
        return data['result']

    def is_report_filterable(self, query_class_obj_code=None, obj_code=None, obj_id=None):
        """
        The ``isReportFilterable`` action.
        
        :param query_class_obj_code: queryClassObjCode (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if query_class_obj_code is not None: params['queryClassObjCode'] = query_class_obj_code
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/isReportFilterable', params)
        return data['result']

    def link_customer(self):
        """
        The ``linkCustomer`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/linkCustomer', params)
        

    def migrate_portal_sections_ppmto_anaconda(self):
        """
        The ``migratePortalSectionsPPMToAnaconda`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/migratePortalSectionsPPMToAnaconda', params)
        

    def send_now(self):
        """
        The ``sendNow`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/sendNow', params)
        

    def unlink_customer(self):
        """
        The ``unlinkCustomer`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unlinkCustomer', params)
        

api.register(PortalSection)


class PortalTab(Object):
    code = 'PTLTAB'
    accessor_ids = Field('accessorIDs')
    customer_id = Field('customerID')
    description = Field('description')
    display_order = Field('displayOrder')
    doc_id = Field('docID')
    ext_ref_id = Field('extRefID')
    is_public = Field('isPublic')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    name_key = Field('nameKey')
    portal_profile_id = Field('portalProfileID')
    tabname = Field('tabname')
    user_id = Field('userID')
    customer = Reference('customer')
    last_updated_by = Reference('lastUpdatedBy')
    portal_profile = Reference('portalProfile')
    user = Reference('user')
    access_rules = Collection('accessRules')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')
    portal_tab_sections = Collection('portalTabSections')

    def advanced_copy(self, new_name=None, advanced_copies=None):
        """
        The ``advancedCopy`` action.
        
        :param new_name: newName (type: ``string``)
        :param advanced_copies: advancedCopies (type: ``map``)
        :return: ``string``
        """
        params = {}
        if new_name is not None: params['newName'] = new_name
        if advanced_copies is not None: params['advancedCopies'] = advanced_copies
        data = self.session.put(self.api_url()+'/advancedCopy', params)
        return data['result']

    def export_dashboard(self, dashboard_exports=None, dashboard_export_options=None):
        """
        The ``exportDashboard`` action.
        
        :param dashboard_exports: dashboardExports (type: ``string[]``)
        :param dashboard_export_options: dashboardExportOptions (type: ``map``)
        :return: ``map``
        """
        params = {}
        if dashboard_exports is not None: params['dashboardExports'] = dashboard_exports
        if dashboard_export_options is not None: params['dashboardExportOptions'] = dashboard_export_options
        data = self.session.put(self.api_url()+'/exportDashboard', params)
        return data['result']

    def migrate_custom_tab_user_prefs(self, user_ids=None):
        """
        The ``migrateCustomTabUserPrefs`` action.
        
        :param user_ids: userIDs (type: ``string[]``)
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        data = self.session.put(self.api_url()+'/migrateCustomTabUserPrefs', params)
        

api.register(PortalTab)


class PortalTabSection(Object):
    code = 'PRTBSC'
    area = Field('area')
    calendar_portal_section_id = Field('calendarPortalSectionID')
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    external_section_id = Field('externalSectionID')
    internal_section_id = Field('internalSectionID')
    portal_section_obj_code = Field('portalSectionObjCode')
    portal_section_obj_id = Field('portalSectionObjID')
    portal_tab_id = Field('portalTabID')
    calendar_portal_section = Reference('calendarPortalSection')
    customer = Reference('customer')
    external_section = Reference('externalSection')
    internal_section = Reference('internalSection')
    portal_tab = Reference('portalTab')

api.register(PortalTabSection)


class Portfolio(Object):
    code = 'PORT'
    accessor_ids = Field('accessorIDs')
    aligned = Field('aligned')
    alignment_score_card_id = Field('alignmentScoreCardID')
    audit_types = Field('auditTypes')
    budget = Field('budget')
    category_id = Field('categoryID')
    currency = Field('currency')
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_documents = Field('hasDocuments')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    is_active = Field('isActive')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    net_value = Field('netValue')
    on_budget = Field('onBudget')
    on_time = Field('onTime')
    owner_id = Field('ownerID')
    roi = Field('roi')
    alignment_score_card = Reference('alignmentScoreCard')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    owner = Reference('owner')
    access_rules = Collection('accessRules')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    groups = Collection('groups')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')
    programs = Collection('programs')
    projects = Collection('projects')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

api.register(Portfolio)


class Predecessor(Object):
    code = 'PRED'
    customer_id = Field('customerID')
    is_cp = Field('isCP')
    is_enforced = Field('isEnforced')
    lag_days = Field('lagDays')
    lag_type = Field('lagType')
    predecessor_id = Field('predecessorID')
    predecessor_type = Field('predecessorType')
    successor_id = Field('successorID')
    customer = Reference('customer')
    predecessor = Reference('predecessor')
    successor = Reference('successor')

api.register(Predecessor)


class Preference(Object):
    code = 'PROSET'
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    value = Field('value')
    app_global = Reference('appGlobal')
    customer = Reference('customer')

api.register(Preference)


class Program(Object):
    code = 'PRGM'
    accessor_ids = Field('accessorIDs')
    audit_types = Field('auditTypes')
    category_id = Field('categoryID')
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_documents = Field('hasDocuments')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    owner_id = Field('ownerID')
    portfolio_id = Field('portfolioID')
    security_ancestors_disabled = Field('securityAncestorsDisabled')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    owner = Reference('owner')
    portfolio = Reference('portfolio')
    access_rules = Collection('accessRules')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')
    projects = Collection('projects')
    security_ancestors = Collection('securityAncestors')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def move(self, portfolio_id=None, options=None):
        """
        The ``move`` action.
        
        :param portfolio_id: portfolioID (type: ``string``)
        :param options: options (type: ``string[]``)
        """
        params = {}
        if portfolio_id is not None: params['portfolioID'] = portfolio_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/move', params)
        

api.register(Program)


class Project(Object):
    code = 'PROJ'
    bccompletion_state = Field('BCCompletionState')
    url = Field('URL')
    accessor_ids = Field('accessorIDs')
    actual_benefit = Field('actualBenefit')
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration_expression = Field('actualDurationExpression')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_expense_cost = Field('actualExpenseCost')
    actual_hours_last_month = Field('actualHoursLastMonth')
    actual_hours_last_three_months = Field('actualHoursLastThreeMonths')
    actual_hours_this_month = Field('actualHoursThisMonth')
    actual_hours_two_months_ago = Field('actualHoursTwoMonthsAgo')
    actual_labor_cost = Field('actualLaborCost')
    actual_revenue = Field('actualRevenue')
    actual_risk_cost = Field('actualRiskCost')
    actual_start_date = Field('actualStartDate')
    actual_value = Field('actualValue')
    actual_work_required = Field('actualWorkRequired')
    actual_work_required_expression = Field('actualWorkRequiredExpression')
    alignment = Field('alignment')
    alignment_score_card_id = Field('alignmentScoreCardID')
    all_approved_hours = Field('allApprovedHours')
    all_unapproved_hours = Field('allUnapprovedHours')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    audit_types = Field('auditTypes')
    auto_baseline_recur_on = Field('autoBaselineRecurOn')
    auto_baseline_recurrence_type = Field('autoBaselineRecurrenceType')
    billed_revenue = Field('billedRevenue')
    budget = Field('budget')
    budget_status = Field('budgetStatus')
    budgeted_completion_date = Field('budgetedCompletionDate')
    budgeted_cost = Field('budgetedCost')
    budgeted_hours = Field('budgetedHours')
    budgeted_labor_cost = Field('budgetedLaborCost')
    budgeted_start_date = Field('budgetedStartDate')
    business_case_status_label = Field('businessCaseStatusLabel')
    category_id = Field('categoryID')
    company_id = Field('companyID')
    completion_type = Field('completionType')
    condition = Field('condition')
    condition_type = Field('conditionType')
    converted_op_task_entry_date = Field('convertedOpTaskEntryDate')
    converted_op_task_name = Field('convertedOpTaskName')
    converted_op_task_originator_id = Field('convertedOpTaskOriginatorID')
    cpi = Field('cpi')
    csi = Field('csi')
    currency = Field('currency')
    current_approval_step_id = Field('currentApprovalStepID')
    customer_id = Field('customerID')
    default_forbidden_contribute_actions = Field('defaultForbiddenContributeActions')
    default_forbidden_manage_actions = Field('defaultForbiddenManageActions')
    default_forbidden_view_actions = Field('defaultForbiddenViewActions')
    deliverable_score_card_id = Field('deliverableScoreCardID')
    deliverable_success_score = Field('deliverableSuccessScore')
    deliverable_success_score_ratio = Field('deliverableSuccessScoreRatio')
    description = Field('description')
    display_order = Field('displayOrder')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    eac = Field('eac')
    eac_calculation_method = Field('eacCalculationMethod')
    enable_auto_baselines = Field('enableAutoBaselines')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    ext_ref_id = Field('extRefID')
    filter_hour_types = Field('filterHourTypes')
    finance_last_update_date = Field('financeLastUpdateDate')
    fixed_cost = Field('fixedCost')
    fixed_end_date = Field('fixedEndDate')
    fixed_revenue = Field('fixedRevenue')
    fixed_start_date = Field('fixedStartDate')
    group_id = Field('groupID')
    has_budget_conflict = Field('hasBudgetConflict')
    has_calc_error = Field('hasCalcError')
    has_completion_constraint = Field('hasCompletionConstraint')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_rate_override = Field('hasRateOverride')
    has_resolvables = Field('hasResolvables')
    has_start_constraint = Field('hasStartConstraint')
    has_timed_notifications = Field('hasTimedNotifications')
    has_timeline_exception = Field('hasTimelineException')
    is_project_dead = Field('isProjectDead')
    is_status_complete = Field('isStatusComplete')
    last_calc_date = Field('lastCalcDate')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_mode = Field('levelingMode')
    lucid_migration_date = Field('lucidMigrationDate')
    milestone_path_id = Field('milestonePathID')
    name = Field('name')
    next_auto_baseline_date = Field('nextAutoBaselineDate')
    number_open_op_tasks = Field('numberOpenOpTasks')
    olv = Field('olv')
    optimization_score = Field('optimizationScore')
    owner_id = Field('ownerID')
    owner_privileges = Field('ownerPrivileges')
    pending_calculation = Field('pendingCalculation')
    pending_update_methods = Field('pendingUpdateMethods')
    percent_complete = Field('percentComplete')
    performance_index_method = Field('performanceIndexMethod')
    personal = Field('personal')
    planned_benefit = Field('plannedBenefit')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_risk_cost = Field('plannedRiskCost')
    planned_start_date = Field('plannedStartDate')
    planned_value = Field('plannedValue')
    pop_account_id = Field('popAccountID')
    portfolio_id = Field('portfolioID')
    portfolio_priority = Field('portfolioPriority')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    program_id = Field('programID')
    progress_status = Field('progressStatus')
    projected_completion_date = Field('projectedCompletionDate')
    projected_start_date = Field('projectedStartDate')
    queue_def_id = Field('queueDefID')
    reference_number = Field('referenceNumber')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_cost = Field('remainingCost')
    remaining_revenue = Field('remainingRevenue')
    remaining_risk_cost = Field('remainingRiskCost')
    resource_pool_id = Field('resourcePoolID')
    risk = Field('risk')
    risk_performance_index = Field('riskPerformanceIndex')
    roi = Field('roi')
    schedule_id = Field('scheduleID')
    schedule_mode = Field('scheduleMode')
    security_ancestors_disabled = Field('securityAncestorsDisabled')
    selected_on_portfolio_optimizer = Field('selectedOnPortfolioOptimizer')
    show_condition = Field('showCondition')
    show_status = Field('showStatus')
    spi = Field('spi')
    sponsor_id = Field('sponsorID')
    status = Field('status')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    summary_completion_type = Field('summaryCompletionType')
    team_id = Field('teamID')
    template_id = Field('templateID')
    timeline_exception_info = Field('timelineExceptionInfo')
    total_hours = Field('totalHours')
    total_op_task_count = Field('totalOpTaskCount')
    total_task_count = Field('totalTaskCount')
    update_type = Field('updateType')
    version = Field('version')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    alignment_score_card = Reference('alignmentScoreCard')
    approval_process = Reference('approvalProcess')
    category = Reference('category')
    company = Reference('company')
    converted_op_task_originator = Reference('convertedOpTaskOriginator')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    default_baseline = Reference('defaultBaseline')
    deliverable_score_card = Reference('deliverableScoreCard')
    entered_by = Reference('enteredBy')
    exchange_rate = Reference('exchangeRate')
    group = Reference('group')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    milestone_path = Reference('milestonePath')
    owner = Reference('owner')
    pop_account = Reference('popAccount')
    portfolio = Reference('portfolio')
    program = Reference('program')
    project = Reference('project')
    queue_def = Reference('queueDef')
    rejection_issue = Reference('rejectionIssue')
    resource_pool = Reference('resourcePool')
    schedule = Reference('schedule')
    sharing_settings = Reference('sharingSettings')
    sponsor = Reference('sponsor')
    submitted_by = Reference('submittedBy')
    team = Reference('team')
    template = Reference('template')
    access_rules = Collection('accessRules')
    alignment_values = Collection('alignmentValues')
    all_hours = Collection('allHours')
    all_priorities = Collection('allPriorities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    awaiting_approvals = Collection('awaitingApprovals')
    baselines = Collection('baselines')
    billing_records = Collection('billingRecords')
    deliverable_values = Collection('deliverableValues')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    exchange_rates = Collection('exchangeRates')
    expenses = Collection('expenses')
    hour_types = Collection('hourTypes')
    hours = Collection('hours')
    notification_records = Collection('notificationRecords')
    object_categories = Collection('objectCategories')
    open_op_tasks = Collection('openOpTasks')
    parameter_values = Collection('parameterValues')
    project_user_roles = Collection('projectUserRoles')
    project_users = Collection('projectUsers')
    rates = Collection('rates')
    resolvables = Collection('resolvables')
    resource_allocations = Collection('resourceAllocations')
    risks = Collection('risks')
    roles = Collection('roles')
    routing_rules = Collection('routingRules')
    security_ancestors = Collection('securityAncestors')
    tasks = Collection('tasks')
    updates = Collection('updates')

    def approve_approval(self, user_id=None, approval_username=None, approval_password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``approveApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param approval_username: approvalUsername (type: ``string``)
        :param approval_password: approvalPassword (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if approval_username is not None: params['approvalUsername'] = approval_username
        if approval_password is not None: params['approvalPassword'] = approval_password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/approveApproval', params)
        

    def async_delete(self, projects_to_delete=None, force=None):
        """
        The ``asyncDelete`` action.
        
        :param projects_to_delete: projectsToDelete (type: ``string[]``)
        :param force: force (type: ``boolean``)
        :return: ``string``
        """
        params = {}
        if projects_to_delete is not None: params['projectsToDelete'] = projects_to_delete
        if force is not None: params['force'] = force
        data = self.session.put(self.api_url()+'/asyncDelete', params)
        return data['result']

    def attach_template(self, template_id=None, predecessor_task_id=None, parent_task_id=None, exclude_template_task_ids=None, options=None):
        """
        The ``attachTemplate`` action.
        
        :param template_id: templateID (type: ``string``)
        :param predecessor_task_id: predecessorTaskID (type: ``string``)
        :param parent_task_id: parentTaskID (type: ``string``)
        :param exclude_template_task_ids: excludeTemplateTaskIDs (type: ``string[]``)
        :param options: options (type: ``string[]``)
        :return: ``string``
        """
        params = {}
        if template_id is not None: params['templateID'] = template_id
        if predecessor_task_id is not None: params['predecessorTaskID'] = predecessor_task_id
        if parent_task_id is not None: params['parentTaskID'] = parent_task_id
        if exclude_template_task_ids is not None: params['excludeTemplateTaskIDs'] = exclude_template_task_ids
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/attachTemplate', params)
        return data['result']

    def attach_template_with_parameter_values(self, project=None, template_id=None, predecessor_task_id=None, parent_task_id=None, exclude_template_task_ids=None, options=None):
        """
        The ``attachTemplateWithParameterValues`` action.
        
        :param project: project (type: ``Project``)
        :param template_id: templateID (type: ``string``)
        :param predecessor_task_id: predecessorTaskID (type: ``string``)
        :param parent_task_id: parentTaskID (type: ``string``)
        :param exclude_template_task_ids: excludeTemplateTaskIDs (type: ``string[]``)
        :param options: options (type: ``string[]``)
        :return: ``string``
        """
        params = {}
        if project is not None: params['project'] = project
        if template_id is not None: params['templateID'] = template_id
        if predecessor_task_id is not None: params['predecessorTaskID'] = predecessor_task_id
        if parent_task_id is not None: params['parentTaskID'] = parent_task_id
        if exclude_template_task_ids is not None: params['excludeTemplateTaskIDs'] = exclude_template_task_ids
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/attachTemplateWithParameterValues', params)
        return data['result']

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def calculate_finance(self):
        """
        The ``calculateFinance`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateFinance', params)
        

    def calculate_project_score_values(self, type=None):
        """
        The ``calculateProjectScoreValues`` action.
        
        :param type: type (type: ``com.attask.common.constants.ScoreCardTypeEnum``)
        """
        params = {}
        if type is not None: params['type'] = type
        data = self.session.put(self.api_url()+'/calculateProjectScoreValues', params)
        

    def calculate_timeline(self):
        """
        The ``calculateTimeline`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateTimeline', params)
        

    def create_project_with_override(self, project=None, exchange_rate=None):
        """
        The ``createProjectWithOverride`` action.
        
        :param project: project (type: ``Project``)
        :param exchange_rate: exchangeRate (type: ``ExchangeRate``)
        :return: ``string``
        """
        params = {}
        if project is not None: params['project'] = project
        if exchange_rate is not None: params['exchangeRate'] = exchange_rate
        data = self.session.put(self.api_url()+'/createProjectWithOverride', params)
        return data['result']

    def export_as_msproject_file(self):
        """
        The ``exportAsMSProjectFile`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/exportAsMSProjectFile', params)
        return data['result']

    def export_business_case(self):
        """
        The ``exportBusinessCase`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/exportBusinessCase', params)
        return data['result']

    def get_help_desk_user_can_add_issue(self):
        """
        The ``getHelpDeskUserCanAddIssue`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getHelpDeskUserCanAddIssue', params)
        return data['result']

    def get_project_currency(self):
        """
        The ``getProjectCurrency`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getProjectCurrency', params)
        return data['result']

    def import_msproject_file(self, file_handle=None, project_name=None):
        """
        The ``importMSProjectFile`` action.
        
        :param file_handle: fileHandle (type: ``string``)
        :param project_name: projectName (type: ``string``)
        :return: ``string``
        """
        params = {}
        if file_handle is not None: params['fileHandle'] = file_handle
        if project_name is not None: params['projectName'] = project_name
        data = self.session.put(self.api_url()+'/importMSProjectFile', params)
        return data['result']

    def recall_approval(self):
        """
        The ``recallApproval`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/recallApproval', params)
        

    def reject_approval(self, user_id=None, approval_username=None, approval_password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``rejectApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param approval_username: approvalUsername (type: ``string``)
        :param approval_password: approvalPassword (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if approval_username is not None: params['approvalUsername'] = approval_username
        if approval_password is not None: params['approvalPassword'] = approval_password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/rejectApproval', params)
        

    def remove_users_from_project(self, user_ids=None):
        """
        The ``removeUsersFromProject`` action.
        
        :param user_ids: userIDs (type: ``string[]``)
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        data = self.session.put(self.api_url()+'/removeUsersFromProject', params)
        

    def save_project_as_template(self, template_name=None, exclude_ids=None, options=None):
        """
        The ``saveProjectAsTemplate`` action.
        
        :param template_name: templateName (type: ``string``)
        :param exclude_ids: excludeIDs (type: ``string[]``)
        :param options: options (type: ``string[]``)
        :return: ``string``
        """
        params = {}
        if template_name is not None: params['templateName'] = template_name
        if exclude_ids is not None: params['excludeIDs'] = exclude_ids
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/saveProjectAsTemplate', params)
        return data['result']

    def set_budget_to_schedule(self):
        """
        The ``setBudgetToSchedule`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/setBudgetToSchedule', params)
        

api.register(Project)


class ProjectUser(Object):
    code = 'PRTU'
    customer_id = Field('customerID')
    project_id = Field('projectID')
    user_id = Field('userID')
    customer = Reference('customer')
    project = Reference('project')
    user = Reference('user')

api.register(ProjectUser)


class ProjectUserRole(Object):
    code = 'PTEAM'
    customer_id = Field('customerID')
    project_id = Field('projectID')
    role_id = Field('roleID')
    user_id = Field('userID')
    customer = Reference('customer')
    project = Reference('project')
    role = Reference('role')
    user = Reference('user')

api.register(ProjectUserRole)


class QueueDef(Object):
    code = 'QUED'
    accessor_ids = Field('accessorIDs')
    add_op_task_style = Field('addOpTaskStyle')
    allowed_legacy_queue_topic_ids = Field('allowedLegacyQueueTopicIDs')
    allowed_op_task_types = Field('allowedOpTaskTypes')
    allowed_queue_topic_ids = Field('allowedQueueTopicIDs')
    customer_id = Field('customerID')
    default_approval_process_id = Field('defaultApprovalProcessID')
    default_category_id = Field('defaultCategoryID')
    default_duration_expression = Field('defaultDurationExpression')
    default_duration_minutes = Field('defaultDurationMinutes')
    default_duration_unit = Field('defaultDurationUnit')
    default_route_id = Field('defaultRouteID')
    default_topic_group_id = Field('defaultTopicGroupID')
    ext_ref_id = Field('extRefID')
    has_queue_topics = Field('hasQueueTopics')
    is_public = Field('isPublic')
    project_id = Field('projectID')
    requestor_core_action = Field('requestorCoreAction')
    requestor_forbidden_actions = Field('requestorForbiddenActions')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    share_mode = Field('shareMode')
    template_id = Field('templateID')
    visible_op_task_fields = Field('visibleOpTaskFields')
    customer = Reference('customer')
    default_approval_process = Reference('defaultApprovalProcess')
    default_category = Reference('defaultCategory')
    default_route = Reference('defaultRoute')
    project = Reference('project')
    template = Reference('template')
    object_categories = Collection('objectCategories')
    queue_topics = Collection('queueTopics')

api.register(QueueDef)


class QueueTopic(Object):
    code = 'QUET'
    accessor_ids = Field('accessorIDs')
    allowed_op_task_types = Field('allowedOpTaskTypes')
    allowed_op_task_types_pretty_print = Field('allowedOpTaskTypesPrettyPrint')
    customer_id = Field('customerID')
    default_approval_process_id = Field('defaultApprovalProcessID')
    default_category_id = Field('defaultCategoryID')
    default_duration = Field('defaultDuration')
    default_duration_expression = Field('defaultDurationExpression')
    default_duration_minutes = Field('defaultDurationMinutes')
    default_duration_unit = Field('defaultDurationUnit')
    default_route_id = Field('defaultRouteID')
    description = Field('description')
    ext_ref_id = Field('extRefID')
    indented_name = Field('indentedName')
    name = Field('name')
    parent_topic_group_id = Field('parentTopicGroupID')
    parent_topic_id = Field('parentTopicID')
    queue_def_id = Field('queueDefID')
    customer = Reference('customer')
    default_approval_process = Reference('defaultApprovalProcess')
    default_category = Reference('defaultCategory')
    default_route = Reference('defaultRoute')
    parent_topic = Reference('parentTopic')
    parent_topic_group = Reference('parentTopicGroup')
    queue_def = Reference('queueDef')
    object_categories = Collection('objectCategories')

api.register(QueueTopic)


class QueueTopicGroup(Object):
    code = 'QUETGP'
    accessor_ids = Field('accessorIDs')
    associated_topics = Field('associatedTopics')
    customer_id = Field('customerID')
    description = Field('description')
    name = Field('name')
    parent_id = Field('parentID')
    queue_def_id = Field('queueDefID')
    customer = Reference('customer')
    parent = Reference('parent')
    queue_def = Reference('queueDef')
    queue_topic_groups = Collection('queueTopicGroups')
    queue_topics = Collection('queueTopics')

api.register(QueueTopicGroup)


class Rate(Object):
    code = 'RATE'
    accessor_ids = Field('accessorIDs')
    company_id = Field('companyID')
    customer_id = Field('customerID')
    ext_ref_id = Field('extRefID')
    project_id = Field('projectID')
    rate_value = Field('rateValue')
    role_id = Field('roleID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    template_id = Field('templateID')
    company = Reference('company')
    customer = Reference('customer')
    project = Reference('project')
    role = Reference('role')
    template = Reference('template')

api.register(Rate)


class Recent(Object):
    code = 'RECENT'
    customer_id = Field('customerID')
    last_viewed_date = Field('lastViewedDate')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    user_id = Field('userID')
    customer = Reference('customer')
    user = Reference('user')

    def update_last_viewed_object(self):
        """
        The ``updateLastViewedObject`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/updateLastViewedObject', params)
        return data['result']

api.register(Recent)


class RecentMenuItem(Object):
    code = 'RECENTMENUITEM'
    allowed_actions = Field('allowedActions')
    date_added = Field('dateAdded')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    recent_item_string = Field('recentItemString')

    def bulk_delete_recent(self, obj_code=None, obj_ids=None):
        """
        The ``bulkDeleteRecent`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_ids: objIDs (type: ``string[]``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_ids is not None: params['objIDs'] = obj_ids
        data = self.session.put(self.api_url()+'/bulkDeleteRecent', params)
        

    def delete_recent(self, obj_code=None, obj_id=None):
        """
        The ``deleteRecent`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/deleteRecent', params)
        

    def rotate_recent_menu(self, obj_code=None, obj_id=None):
        """
        The ``rotateRecentMenu`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/rotateRecentMenu', params)
        

api.register(RecentMenuItem)


class RecentUpdate(Object):
    code = 'RUPDTE'
    author_id = Field('authorID')
    author_name = Field('authorName')
    customer_id = Field('customerID')
    entry_date = Field('entryDate')
    is_private = Field('isPrivate')
    issue_id = Field('issueID')
    issue_name = Field('issueName')
    iteration_id = Field('iterationID')
    iteration_name = Field('iterationName')
    last_updated_on_date = Field('lastUpdatedOnDate')
    latest_comment = Field('latestComment')
    latest_comment_author_id = Field('latestCommentAuthorID')
    latest_comment_author_name = Field('latestCommentAuthorName')
    latest_comment_entry_date = Field('latestCommentEntryDate')
    latest_comment_id = Field('latestCommentID')
    number_of_comments = Field('numberOfComments')
    project_id = Field('projectID')
    project_name = Field('projectName')
    task_id = Field('taskID')
    task_name = Field('taskName')
    team_id = Field('teamID')
    thread_id = Field('threadID')
    update = Field('update')
    update_id = Field('updateID')
    user_id = Field('userID')
    customer = Reference('customer')

api.register(RecentUpdate)


class RecurrenceRule(Object):
    code = 'RECR'
    customer_id = Field('customerID')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    duration_unit = Field('durationUnit')
    end_date = Field('endDate')
    recur_on = Field('recurOn')
    recurrence_count = Field('recurrenceCount')
    recurrence_interval = Field('recurrenceInterval')
    recurrence_type = Field('recurrenceType')
    schedule_id = Field('scheduleID')
    start_date = Field('startDate')
    task_id = Field('taskID')
    template_task_id = Field('templateTaskID')
    use_end_date = Field('useEndDate')
    customer = Reference('customer')
    schedule = Reference('schedule')
    task = Reference('task')
    template_task = Reference('templateTask')

api.register(RecurrenceRule)


class ReportFolder(Object):
    code = 'RPTFDR'
    customer_id = Field('customerID')
    name = Field('name')
    customer = Reference('customer')

api.register(ReportFolder)


class Reseller(Object):
    code = 'RSELR'
    address = Field('address')
    address2 = Field('address2')
    city = Field('city')
    country = Field('country')
    description = Field('description')
    email = Field('email')
    ext_ref_id = Field('extRefID')
    is_active = Field('isActive')
    name = Field('name')
    phone_number = Field('phoneNumber')
    postal_code = Field('postalCode')
    state = Field('state')
    account_reps = Collection('accountReps')

api.register(Reseller)


class ReservedTime(Object):
    code = 'RESVT'
    customer_id = Field('customerID')
    end_date = Field('endDate')
    start_date = Field('startDate')
    task_id = Field('taskID')
    user_id = Field('userID')
    customer = Reference('customer')
    task = Reference('task')
    user = Reference('user')

api.register(ReservedTime)


class ResourceAllocation(Object):
    code = 'RSALLO'
    accessor_ids = Field('accessorIDs')
    allocation_date = Field('allocationDate')
    budgeted_hours = Field('budgetedHours')
    customer_id = Field('customerID')
    is_split = Field('isSplit')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    project_id = Field('projectID')
    projected_scheduled_hours = Field('projectedScheduledHours')
    resource_pool_id = Field('resourcePoolID')
    role_id = Field('roleID')
    scheduled_hours = Field('scheduledHours')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    customer = Reference('customer')
    project = Reference('project')
    resource_pool = Reference('resourcePool')
    role = Reference('role')

api.register(ResourceAllocation)


class ResourcePool(Object):
    code = 'RSPOOL'
    customer_id = Field('customerID')
    description = Field('description')
    display_order = Field('displayOrder')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    customer = Reference('customer')
    resource_allocations = Collection('resourceAllocations')
    roles = Collection('roles')
    users = Collection('users')

api.register(ResourcePool)


class Risk(Object):
    code = 'RISK'
    accessor_ids = Field('accessorIDs')
    actual_cost = Field('actualCost')
    customer_id = Field('customerID')
    description = Field('description')
    estimated_effect = Field('estimatedEffect')
    ext_ref_id = Field('extRefID')
    mitigation_cost = Field('mitigationCost')
    mitigation_description = Field('mitigationDescription')
    probability = Field('probability')
    project_id = Field('projectID')
    risk_type_id = Field('riskTypeID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    status = Field('status')
    template_id = Field('templateID')
    customer = Reference('customer')
    project = Reference('project')
    risk_type = Reference('riskType')
    template = Reference('template')

api.register(Risk)


class RiskType(Object):
    code = 'RSKTYP'
    customer_id = Field('customerID')
    description = Field('description')
    ext_ref_id = Field('extRefID')
    name = Field('name')
    customer = Reference('customer')

    def has_reference(self, ids=None):
        """
        The ``hasReference`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/hasReference', params)
        return data['result']

api.register(RiskType)


class Role(Object):
    code = 'ROLE'
    billing_per_hour = Field('billingPerHour')
    cost_per_hour = Field('costPerHour')
    customer_id = Field('customerID')
    default_interface = Field('defaultInterface')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    layout_template_id = Field('layoutTemplateID')
    max_users = Field('maxUsers')
    name = Field('name')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    layout_template = Reference('layoutTemplate')

    def add_early_access(self, ids=None):
        """
        The ``addEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/addEarlyAccess', params)
        

    def delete_early_access(self, ids=None):
        """
        The ``deleteEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/deleteEarlyAccess', params)
        

    def has_reference(self, ids=None):
        """
        The ``hasReference`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/hasReference', params)
        return data['result']

api.register(Role)


class RoutingRule(Object):
    code = 'RRUL'
    accessor_ids = Field('accessorIDs')
    customer_id = Field('customerID')
    default_assigned_to_id = Field('defaultAssignedToID')
    default_project_id = Field('defaultProjectID')
    default_role_id = Field('defaultRoleID')
    default_team_id = Field('defaultTeamID')
    description = Field('description')
    name = Field('name')
    project_id = Field('projectID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    template_id = Field('templateID')
    customer = Reference('customer')
    default_assigned_to = Reference('defaultAssignedTo')
    default_project = Reference('defaultProject')
    default_role = Reference('defaultRole')
    default_team = Reference('defaultTeam')
    project = Reference('project')
    template = Reference('template')

api.register(RoutingRule)


class S3Migration(Object):
    code = 'S3MT'
    customer_id = Field('customerID')
    migration_date = Field('migrationDate')
    status = Field('status')
    customer = Reference('customer')

api.register(S3Migration)


class SSOMapping(Object):
    code = 'SSOMAP'
    attask_attribute = Field('attaskAttribute')
    customer_id = Field('customerID')
    default_attribute = Field('defaultAttribute')
    has_mapping_rules = Field('hasMappingRules')
    override_attribute = Field('overrideAttribute')
    remote_attribute = Field('remoteAttribute')
    sso_option_id = Field('ssoOptionID')
    customer = Reference('customer')
    mapping_rules = Collection('mappingRules')

api.register(SSOMapping)


class SSOMappingRule(Object):
    code = 'SSOMR'
    attask_attribute = Field('attaskAttribute')
    customer_id = Field('customerID')
    matching_rule = Field('matchingRule')
    remote_attribute = Field('remoteAttribute')
    sso_mapping_id = Field('ssoMappingID')
    customer = Reference('customer')

api.register(SSOMappingRule)


class SSOOption(Object):
    code = 'SSOPT'
    ssoenabled = Field('SSOEnabled')
    active_directory_domain = Field('activeDirectoryDomain')
    authentication_type = Field('authenticationType')
    binding_type = Field('bindingType')
    certificate = Field('certificate')
    change_password_url = Field('changePasswordURL')
    customer_id = Field('customerID')
    exclude_users = Field('excludeUsers')
    hosted_entity_id = Field('hostedEntityID')
    is_admin_back_door_access_allowed = Field('isAdminBackDoorAccessAllowed')
    provider_port = Field('providerPort')
    provider_url = Field('providerURL')
    provision_users = Field('provisionUsers')
    remote_entity_id = Field('remoteEntityID')
    require_sslconnection = Field('requireSSLConnection')
    search_attribute = Field('searchAttribute')
    search_base = Field('searchBase')
    signout_url = Field('signoutURL')
    trusted_domain = Field('trustedDomain')
    customer = Reference('customer')
    sso_mappings = Collection('ssoMappings')

    def upload_saml2metadata(self, handle=None):
        """
        The ``uploadSAML2Metadata`` action.
        
        :param handle: handle (type: ``string``)
        :return: ``string``
        """
        params = {}
        if handle is not None: params['handle'] = handle
        data = self.session.put(self.api_url()+'/uploadSAML2Metadata', params)
        return data['result']

    def upload_ssocertificate(self, handle=None):
        """
        The ``uploadSSOCertificate`` action.
        
        :param handle: handle (type: ``string``)
        """
        params = {}
        if handle is not None: params['handle'] = handle
        data = self.session.put(self.api_url()+'/uploadSSOCertificate', params)
        

api.register(SSOOption)


class SSOUsername(Object):
    code = 'SSOUSR'
    customer_id = Field('customerID')
    name = Field('name')
    user_id = Field('userID')

api.register(SSOUsername)


class SandboxMigration(Object):
    code = 'SNDMG'
    customer_id = Field('customerID')
    domain = Field('domain')
    end_date = Field('endDate')
    last_refresh_date = Field('lastRefreshDate')
    last_refresh_duration = Field('lastRefreshDuration')
    notified = Field('notified')
    sandbox_type = Field('sandboxType')
    schedule_date = Field('scheduleDate')
    start_date = Field('startDate')
    status = Field('status')
    user_id = Field('userID')
    customer = Reference('customer')
    user = Reference('user')

    def cancel_scheduled_migration(self):
        """
        The ``cancelScheduledMigration`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/cancelScheduledMigration', params)
        

    def migrate_now(self):
        """
        The ``migrateNow`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/migrateNow', params)
        

    def migration_estimate(self):
        """
        The ``migrationEstimate`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/migrationEstimate', params)
        return data['result']

    def migration_queue_duration(self):
        """
        The ``migrationQueueDuration`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/migrationQueueDuration', params)
        return data['result']

    def schedule_migration(self, schedule_date=None):
        """
        The ``scheduleMigration`` action.
        
        :param schedule_date: scheduleDate (type: ``dateTime``)
        """
        params = {}
        if schedule_date is not None: params['scheduleDate'] = schedule_date
        data = self.session.put(self.api_url()+'/scheduleMigration', params)
        

api.register(SandboxMigration)


class Schedule(Object):
    code = 'SCHED'
    customer_id = Field('customerID')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    friday = Field('friday')
    group_id = Field('groupID')
    has_non_work_days = Field('hasNonWorkDays')
    is_default = Field('isDefault')
    monday = Field('monday')
    name = Field('name')
    saturday = Field('saturday')
    sunday = Field('sunday')
    thursday = Field('thursday')
    time_zone = Field('timeZone')
    tuesday = Field('tuesday')
    wednesday = Field('wednesday')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    group = Reference('group')
    non_work_days = Collection('nonWorkDays')
    other_groups = Collection('otherGroups')

    def get_earliest_work_time_of_day(self, date=None):
        """
        The ``getEarliestWorkTimeOfDay`` action.
        
        :param date: date (type: ``dateTime``)
        :return: ``dateTime``
        """
        params = {}
        if date is not None: params['date'] = date
        data = self.session.put(self.api_url()+'/getEarliestWorkTimeOfDay', params)
        return data['result']

    def get_latest_work_time_of_day(self, date=None):
        """
        The ``getLatestWorkTimeOfDay`` action.
        
        :param date: date (type: ``dateTime``)
        :return: ``dateTime``
        """
        params = {}
        if date is not None: params['date'] = date
        data = self.session.put(self.api_url()+'/getLatestWorkTimeOfDay', params)
        return data['result']

    def get_next_completion_date(self, date=None, cost_in_minutes=None):
        """
        The ``getNextCompletionDate`` action.
        
        :param date: date (type: ``dateTime``)
        :param cost_in_minutes: costInMinutes (type: ``int``)
        :return: ``dateTime``
        """
        params = {}
        if date is not None: params['date'] = date
        if cost_in_minutes is not None: params['costInMinutes'] = cost_in_minutes
        data = self.session.put(self.api_url()+'/getNextCompletionDate', params)
        return data['result']

    def get_next_start_date(self, date=None):
        """
        The ``getNextStartDate`` action.
        
        :param date: date (type: ``dateTime``)
        :return: ``dateTime``
        """
        params = {}
        if date is not None: params['date'] = date
        data = self.session.put(self.api_url()+'/getNextStartDate', params)
        return data['result']

    def has_reference(self, ids=None):
        """
        The ``hasReference`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/hasReference', params)
        return data['result']

api.register(Schedule)


class ScheduledReport(Object):
    code = 'SCHREP'
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    external_emails = Field('externalEmails')
    format = Field('format')
    group_ids = Field('groupIDs')
    last_runtime_milliseconds = Field('lastRuntimeMilliseconds')
    last_sent_date = Field('lastSentDate')
    name = Field('name')
    page_size = Field('pageSize')
    portal_section_id = Field('portalSectionID')
    recipients = Field('recipients')
    recurrence_rule = Field('recurrenceRule')
    role_ids = Field('roleIDs')
    run_as_user_id = Field('runAsUserID')
    run_as_user_type_ahead = Field('runAsUserTypeAhead')
    sched_time = Field('schedTime')
    schedule = Field('schedule')
    schedule_start = Field('scheduleStart')
    start_date = Field('startDate')
    team_ids = Field('teamIDs')
    ui_obj_code = Field('uiObjCode')
    ui_obj_id = Field('uiObjID')
    user_ids = Field('userIDs')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    portal_section = Reference('portalSection')
    run_as_user = Reference('runAsUser')
    groups = Collection('groups')
    roles = Collection('roles')
    teams = Collection('teams')
    users = Collection('users')

    def send_report_delivery_now(self, user_ids=None, team_ids=None, group_ids=None, role_ids=None, external_emails=None, delivery_options=None):
        """
        The ``sendReportDeliveryNow`` action.
        
        :param user_ids: userIDs (type: ``string[]``)
        :param team_ids: teamIDs (type: ``string[]``)
        :param group_ids: groupIDs (type: ``string[]``)
        :param role_ids: roleIDs (type: ``string[]``)
        :param external_emails: externalEmails (type: ``string``)
        :param delivery_options: deliveryOptions (type: ``map``)
        :return: ``java.lang.Integer``
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        if team_ids is not None: params['teamIDs'] = team_ids
        if group_ids is not None: params['groupIDs'] = group_ids
        if role_ids is not None: params['roleIDs'] = role_ids
        if external_emails is not None: params['externalEmails'] = external_emails
        if delivery_options is not None: params['deliveryOptions'] = delivery_options
        data = self.session.put(self.api_url()+'/sendReportDeliveryNow', params)
        return data['result']

api.register(ScheduledReport)


class ScoreCard(Object):
    code = 'SCORE'
    accessor_ids = Field('accessorIDs')
    customer_id = Field('customerID')
    description = Field('description')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    is_public = Field('isPublic')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    project_id = Field('projectID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    template_id = Field('templateID')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    project = Reference('project')
    template = Reference('template')
    score_card_questions = Collection('scoreCardQuestions')

api.register(ScoreCard)


class ScoreCardAnswer(Object):
    code = 'SCANS'
    customer_id = Field('customerID')
    number_val = Field('numberVal')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    project_id = Field('projectID')
    score_card_id = Field('scoreCardID')
    score_card_option_id = Field('scoreCardOptionID')
    score_card_question_id = Field('scoreCardQuestionID')
    template_id = Field('templateID')
    type = Field('type')
    customer = Reference('customer')
    project = Reference('project')
    score_card = Reference('scoreCard')
    score_card_option = Reference('scoreCardOption')
    score_card_question = Reference('scoreCardQuestion')
    template = Reference('template')

api.register(ScoreCardAnswer)


class ScoreCardOption(Object):
    code = 'SCOPT'
    customer_id = Field('customerID')
    display_order = Field('displayOrder')
    is_default = Field('isDefault')
    is_hidden = Field('isHidden')
    label = Field('label')
    score_card_question_id = Field('scoreCardQuestionID')
    value = Field('value')
    customer = Reference('customer')
    score_card_question = Reference('scoreCardQuestion')

api.register(ScoreCardOption)


class ScoreCardQuestion(Object):
    code = 'SCOREQ'
    customer_id = Field('customerID')
    description = Field('description')
    display_order = Field('displayOrder')
    display_type = Field('displayType')
    name = Field('name')
    score_card_id = Field('scoreCardID')
    weight = Field('weight')
    customer = Reference('customer')
    score_card = Reference('scoreCard')
    score_card_options = Collection('scoreCardOptions')

api.register(ScoreCardQuestion)


class SearchEvent(Object):
    code = 'SRCEVT'
    customer_id = Field('customerID')
    entry_date = Field('entryDate')
    event_obj_code = Field('eventObjCode')
    event_type = Field('eventType')
    obj_ids = Field('objIDs')

api.register(SearchEvent)


class SecurityAncestor(Object):
    code = 'SECANC'
    ancestor_id = Field('ancestorID')
    ancestor_obj_code = Field('ancestorObjCode')
    customer_id = Field('customerID')
    ref_obj_code = Field('refObjCode')
    ref_obj_id = Field('refObjID')
    customer = Reference('customer')

api.register(SecurityAncestor)


class Sequence(Object):
    code = 'SEQ'
    customer_id = Field('customerID')
    seq_name = Field('seqName')
    seq_value = Field('seqValue')
    customer = Reference('customer')

api.register(Sequence)


class SharingSettings(Object):
    code = 'SHRSET'
    accessor_ids = Field('accessorIDs')
    customer_id = Field('customerID')
    op_task_assignment_core_action = Field('opTaskAssignmentCoreAction')
    op_task_assignment_project_core_action = Field('opTaskAssignmentProjectCoreAction')
    op_task_assignment_project_secondary_actions = Field('opTaskAssignmentProjectSecondaryActions')
    op_task_assignment_secondary_actions = Field('opTaskAssignmentSecondaryActions')
    project_id = Field('projectID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    task_assignment_core_action = Field('taskAssignmentCoreAction')
    task_assignment_project_core_action = Field('taskAssignmentProjectCoreAction')
    task_assignment_project_secondary_actions = Field('taskAssignmentProjectSecondaryActions')
    task_assignment_secondary_actions = Field('taskAssignmentSecondaryActions')
    template_id = Field('templateID')
    customer = Reference('customer')
    project = Reference('project')
    template = Reference('template')

api.register(SharingSettings)


class StepApprover(Object):
    code = 'SPAPVR'
    approval_step_id = Field('approvalStepID')
    customer_id = Field('customerID')
    role_id = Field('roleID')
    team_id = Field('teamID')
    user_id = Field('userID')
    wild_card = Field('wildCard')
    approval_step = Reference('approvalStep')
    customer = Reference('customer')
    role = Reference('role')
    team = Reference('team')
    user = Reference('user')

api.register(StepApprover)


class Task(Object):
    code = 'TASK'
    url = Field('URL')
    accessor_ids = Field('accessorIDs')
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration = Field('actualDuration')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_expense_cost = Field('actualExpenseCost')
    actual_labor_cost = Field('actualLaborCost')
    actual_revenue = Field('actualRevenue')
    actual_start_date = Field('actualStartDate')
    actual_work = Field('actualWork')
    actual_work_required = Field('actualWorkRequired')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    assigned_to_id = Field('assignedToID')
    assignments_list_string = Field('assignmentsListString')
    audit_note = Field('auditNote')
    audit_types = Field('auditTypes')
    audit_user_ids = Field('auditUserIDs')
    backlog_order = Field('backlogOrder')
    billing_amount = Field('billingAmount')
    billing_record_id = Field('billingRecordID')
    can_start = Field('canStart')
    category_id = Field('categoryID')
    color = Field('color')
    commit_date = Field('commitDate')
    commit_date_range = Field('commitDateRange')
    completion_pending_date = Field('completionPendingDate')
    condition = Field('condition')
    constraint_date = Field('constraintDate')
    converted_op_task_entry_date = Field('convertedOpTaskEntryDate')
    converted_op_task_name = Field('convertedOpTaskName')
    converted_op_task_originator_id = Field('convertedOpTaskOriginatorID')
    cost_amount = Field('costAmount')
    cost_type = Field('costType')
    cpi = Field('cpi')
    csi = Field('csi')
    current_approval_step_id = Field('currentApprovalStepID')
    customer_id = Field('customerID')
    days_late = Field('daysLate')
    description = Field('description')
    due_date = Field('dueDate')
    duration = Field('duration')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    duration_type = Field('durationType')
    duration_unit = Field('durationUnit')
    eac = Field('eac')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    estimate = Field('estimate')
    ext_ref_id = Field('extRefID')
    group_id = Field('groupID')
    handoff_date = Field('handoffDate')
    has_completion_constraint = Field('hasCompletionConstraint')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_resolvables = Field('hasResolvables')
    has_start_constraint = Field('hasStartConstraint')
    has_timed_notifications = Field('hasTimedNotifications')
    hours_per_point = Field('hoursPerPoint')
    indent = Field('indent')
    is_agile = Field('isAgile')
    is_critical = Field('isCritical')
    is_duration_locked = Field('isDurationLocked')
    is_leveling_excluded = Field('isLevelingExcluded')
    is_ready = Field('isReady')
    is_status_complete = Field('isStatusComplete')
    is_work_required_locked = Field('isWorkRequiredLocked')
    iteration_id = Field('iterationID')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_start_delay = Field('levelingStartDelay')
    leveling_start_delay_expression = Field('levelingStartDelayExpression')
    leveling_start_delay_minutes = Field('levelingStartDelayMinutes')
    master_task_id = Field('masterTaskID')
    milestone_id = Field('milestoneID')
    name = Field('name')
    number_of_children = Field('numberOfChildren')
    number_open_op_tasks = Field('numberOpenOpTasks')
    olv = Field('olv')
    original_duration = Field('originalDuration')
    original_work_required = Field('originalWorkRequired')
    parent_id = Field('parentID')
    parent_lag = Field('parentLag')
    parent_lag_type = Field('parentLagType')
    pending_calculation = Field('pendingCalculation')
    pending_predecessors = Field('pendingPredecessors')
    pending_update_methods = Field('pendingUpdateMethods')
    percent_complete = Field('percentComplete')
    personal = Field('personal')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_duration = Field('plannedDuration')
    planned_duration_minutes = Field('plannedDurationMinutes')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_start_date = Field('plannedStartDate')
    predecessor_expression = Field('predecessorExpression')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    progress_status = Field('progressStatus')
    project_id = Field('projectID')
    projected_completion_date = Field('projectedCompletionDate')
    projected_duration_minutes = Field('projectedDurationMinutes')
    projected_start_date = Field('projectedStartDate')
    recurrence_number = Field('recurrenceNumber')
    recurrence_rule_id = Field('recurrenceRuleID')
    reference_number = Field('referenceNumber')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_duration_minutes = Field('remainingDurationMinutes')
    reserved_time_id = Field('reservedTimeID')
    resource_scope = Field('resourceScope')
    revenue_type = Field('revenueType')
    role_id = Field('roleID')
    security_ancestors_disabled = Field('securityAncestorsDisabled')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    show_commit_date = Field('showCommitDate')
    show_condition = Field('showCondition')
    show_status = Field('showStatus')
    slack_date = Field('slackDate')
    spi = Field('spi')
    status = Field('status')
    status_equates_with = Field('statusEquatesWith')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    task_constraint = Field('taskConstraint')
    task_number = Field('taskNumber')
    task_number_predecessor_string = Field('taskNumberPredecessorString')
    team_id = Field('teamID')
    template_task_id = Field('templateTaskID')
    tracking_mode = Field('trackingMode')
    version = Field('version')
    wbs = Field('wbs')
    work = Field('work')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    work_unit = Field('workUnit')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    billing_record = Reference('billingRecord')
    category = Reference('category')
    converted_op_task_originator = Reference('convertedOpTaskOriginator')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    default_baseline_task = Reference('defaultBaselineTask')
    entered_by = Reference('enteredBy')
    group = Reference('group')
    iteration = Reference('iteration')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    master_task = Reference('masterTask')
    milestone = Reference('milestone')
    parent = Reference('parent')
    primary_assignment = Reference('primaryAssignment')
    project = Reference('project')
    recurrence_rule = Reference('recurrenceRule')
    rejection_issue = Reference('rejectionIssue')
    reserved_time = Reference('reservedTime')
    role = Reference('role')
    submitted_by = Reference('submittedBy')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    template_task = Reference('templateTask')
    work_item = Reference('workItem')
    access_rules = Collection('accessRules')
    all_priorities = Collection('allPriorities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    assignments = Collection('assignments')
    awaiting_approvals = Collection('awaitingApprovals')
    children = Collection('children')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    done_statuses = Collection('doneStatuses')
    expenses = Collection('expenses')
    hours = Collection('hours')
    notification_records = Collection('notificationRecords')
    object_categories = Collection('objectCategories')
    op_tasks = Collection('opTasks')
    open_op_tasks = Collection('openOpTasks')
    parameter_values = Collection('parameterValues')
    predecessors = Collection('predecessors')
    resolvables = Collection('resolvables')
    security_ancestors = Collection('securityAncestors')
    successors = Collection('successors')
    updates = Collection('updates')

    def accept_work(self):
        """
        The ``acceptWork`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/acceptWork', params)
        

    def approve_approval(self, user_id=None, username=None, password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``approveApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/approveApproval', params)
        

    def assign(self, obj_id=None, obj_code=None):
        """
        The ``assign`` action.
        
        :param obj_id: objID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        """
        params = {}
        if obj_id is not None: params['objID'] = obj_id
        if obj_code is not None: params['objCode'] = obj_code
        data = self.session.put(self.api_url()+'/assign', params)
        

    def assign_multiple(self, user_ids=None, role_ids=None, team_id=None):
        """
        The ``assignMultiple`` action.
        
        :param user_ids: userIDs (type: ``string[]``)
        :param role_ids: roleIDs (type: ``string[]``)
        :param team_id: teamID (type: ``string``)
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        if role_ids is not None: params['roleIDs'] = role_ids
        if team_id is not None: params['teamID'] = team_id
        data = self.session.put(self.api_url()+'/assignMultiple', params)
        

    def bulk_copy(self, task_ids=None, project_id=None, parent_id=None, options=None):
        """
        The ``bulkCopy`` action.
        
        :param task_ids: taskIDs (type: ``string[]``)
        :param project_id: projectID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        :param options: options (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if task_ids is not None: params['taskIDs'] = task_ids
        if project_id is not None: params['projectID'] = project_id
        if parent_id is not None: params['parentID'] = parent_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/bulkCopy', params)
        return data['result']

    def bulk_move(self, task_ids=None, project_id=None, parent_id=None, options=None):
        """
        The ``bulkMove`` action.
        
        :param task_ids: taskIDs (type: ``string[]``)
        :param project_id: projectID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        :param options: options (type: ``string[]``)
        """
        params = {}
        if task_ids is not None: params['taskIDs'] = task_ids
        if project_id is not None: params['projectID'] = project_id
        if parent_id is not None: params['parentID'] = parent_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/bulkMove', params)
        

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def calculate_data_extensions(self, ids=None):
        """
        The ``calculateDataExtensions`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/calculateDataExtensions', params)
        

    def convert_to_project(self, project=None, exchange_rate=None):
        """
        The ``convertToProject`` action.
        
        :param project: project (type: ``Project``)
        :param exchange_rate: exchangeRate (type: ``ExchangeRate``)
        :return: ``string``
        """
        params = {}
        if project is not None: params['project'] = project
        if exchange_rate is not None: params['exchangeRate'] = exchange_rate
        data = self.session.put(self.api_url()+'/convertToProject', params)
        return data['result']

    def mark_done(self, status=None):
        """
        The ``markDone`` action.
        
        :param status: status (type: ``string``)
        """
        params = {}
        if status is not None: params['status'] = status
        data = self.session.put(self.api_url()+'/markDone', params)
        

    def mark_not_done(self, assignment_id=None):
        """
        The ``markNotDone`` action.
        
        :param assignment_id: assignmentID (type: ``string``)
        """
        params = {}
        if assignment_id is not None: params['assignmentID'] = assignment_id
        data = self.session.put(self.api_url()+'/markNotDone', params)
        

    def move(self, project_id=None, parent_id=None, options=None):
        """
        The ``move`` action.
        
        :param project_id: projectID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        :param options: options (type: ``string[]``)
        """
        params = {}
        if project_id is not None: params['projectID'] = project_id
        if parent_id is not None: params['parentID'] = parent_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/move', params)
        

    def recall_approval(self):
        """
        The ``recallApproval`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/recallApproval', params)
        

    def reject_approval(self, user_id=None, username=None, password=None, audit_note=None, audit_user_ids=None, send_note_as_email=None):
        """
        The ``rejectApproval`` action.
        
        :param user_id: userID (type: ``string``)
        :param username: username (type: ``string``)
        :param password: password (type: ``string``)
        :param audit_note: auditNote (type: ``string``)
        :param audit_user_ids: auditUserIDs (type: ``string[]``)
        :param send_note_as_email: sendNoteAsEmail (type: ``boolean``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if username is not None: params['username'] = username
        if password is not None: params['password'] = password
        if audit_note is not None: params['auditNote'] = audit_note
        if audit_user_ids is not None: params['auditUserIDs'] = audit_user_ids
        if send_note_as_email is not None: params['sendNoteAsEmail'] = send_note_as_email
        data = self.session.put(self.api_url()+'/rejectApproval', params)
        

    def reply_to_assignment(self, note_text=None, commit_date=None):
        """
        The ``replyToAssignment`` action.
        
        :param note_text: noteText (type: ``string``)
        :param commit_date: commitDate (type: ``dateTime``)
        """
        params = {}
        if note_text is not None: params['noteText'] = note_text
        if commit_date is not None: params['commitDate'] = commit_date
        data = self.session.put(self.api_url()+'/replyToAssignment', params)
        

    def timed_notifications(self, notification_ids=None):
        """
        The ``timedNotifications`` action.
        
        :param notification_ids: notificationIDs (type: ``string[]``)
        """
        params = {}
        if notification_ids is not None: params['notificationIDs'] = notification_ids
        data = self.session.put(self.api_url()+'/timedNotifications', params)
        

    def unaccept_work(self):
        """
        The ``unacceptWork`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unacceptWork', params)
        

    def unassign(self, user_id=None):
        """
        The ``unassign`` action.
        
        :param user_id: userID (type: ``string``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/unassign', params)
        

    def unassign_occurrences(self, user_id=None):
        """
        The ``unassignOccurrences`` action.
        
        :param user_id: userID (type: ``string``)
        :return: ``string[]``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/unassignOccurrences', params)
        return data['result']

    def add_comment(self, text):
        """
        Add a comment to the current object containing the supplied text.

        The new :class:`Comment` instance is returned, it does not need to be
        saved.
        """

        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.code,
            obj_id = self.id
        )
        comment.save()
        return comment

api.register(Task)


class Team(Object):
    code = 'TEAMOB'
    customer_id = Field('customerID')
    default_interface = Field('defaultInterface')
    description = Field('description')
    estimate_by_hours = Field('estimateByHours')
    hours_per_point = Field('hoursPerPoint')
    is_agile = Field('isAgile')
    is_standard_issue_list = Field('isStandardIssueList')
    layout_template_id = Field('layoutTemplateID')
    my_work_view_id = Field('myWorkViewID')
    name = Field('name')
    op_task_bug_report_statuses = Field('opTaskBugReportStatuses')
    op_task_change_order_statuses = Field('opTaskChangeOrderStatuses')
    op_task_issue_statuses = Field('opTaskIssueStatuses')
    op_task_request_statuses = Field('opTaskRequestStatuses')
    owner_id = Field('ownerID')
    requests_view_id = Field('requestsViewID')
    schedule_id = Field('scheduleID')
    task_statuses = Field('taskStatuses')
    team_story_board_statuses = Field('teamStoryBoardStatuses')
    team_type = Field('teamType')
    customer = Reference('customer')
    layout_template = Reference('layoutTemplate')
    my_work_view = Reference('myWorkView')
    owner = Reference('owner')
    requests_view = Reference('requestsView')
    schedule = Reference('schedule')
    backlog_tasks = Collection('backlogTasks')
    team_member_roles = Collection('teamMemberRoles')
    team_members = Collection('teamMembers')
    updates = Collection('updates')
    users = Collection('users')

    def add_early_access(self, ids=None):
        """
        The ``addEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/addEarlyAccess', params)
        

    def delete_early_access(self, ids=None):
        """
        The ``deleteEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/deleteEarlyAccess', params)
        

    def move_tasks_on_team_backlog(self, team_id=None, start_number=None, end_number=None, move_to_number=None, moving_task_ids=None):
        """
        The ``moveTasksOnTeamBacklog`` action.
        
        :param team_id: teamID (type: ``string``)
        :param start_number: startNumber (type: ``int``)
        :param end_number: endNumber (type: ``int``)
        :param move_to_number: moveToNumber (type: ``int``)
        :param moving_task_ids: movingTaskIDs (type: ``string[]``)
        """
        params = {}
        if team_id is not None: params['teamID'] = team_id
        if start_number is not None: params['startNumber'] = start_number
        if end_number is not None: params['endNumber'] = end_number
        if move_to_number is not None: params['moveToNumber'] = move_to_number
        if moving_task_ids is not None: params['movingTaskIDs'] = moving_task_ids
        data = self.session.put(self.api_url()+'/moveTasksOnTeamBacklog', params)


api.register(Team)


class TeamMember(Object):
    code = 'TEAMMB'
    adhoc_team = Field('adhocTeam')
    customer_id = Field('customerID')
    has_assign_permissions = Field('hasAssignPermissions')
    team_id = Field('teamID')
    user_id = Field('userID')
    customer = Reference('customer')
    team = Reference('team')
    user = Reference('user')

api.register(TeamMember)


class TeamMemberRole(Object):
    code = 'TEAMMR'
    customer_id = Field('customerID')
    role_id = Field('roleID')
    team_id = Field('teamID')
    user_id = Field('userID')
    customer = Reference('customer')
    role = Reference('role')
    team = Reference('team')
    user = Reference('user')

api.register(TeamMemberRole)


class Template(Object):
    code = 'TMPL'
    url = Field('URL')
    accessor_ids = Field('accessorIDs')
    approval_process_id = Field('approvalProcessID')
    auto_baseline_recur_on = Field('autoBaselineRecurOn')
    auto_baseline_recurrence_type = Field('autoBaselineRecurrenceType')
    budget = Field('budget')
    category_id = Field('categoryID')
    company_id = Field('companyID')
    completion_day = Field('completionDay')
    completion_type = Field('completionType')
    condition_type = Field('conditionType')
    currency = Field('currency')
    customer_id = Field('customerID')
    default_forbidden_contribute_actions = Field('defaultForbiddenContributeActions')
    default_forbidden_manage_actions = Field('defaultForbiddenManageActions')
    default_forbidden_view_actions = Field('defaultForbiddenViewActions')
    deliverable_score_card_id = Field('deliverableScoreCardID')
    deliverable_success_score = Field('deliverableSuccessScore')
    description = Field('description')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    enable_auto_baselines = Field('enableAutoBaselines')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    filter_hour_types = Field('filterHourTypes')
    fixed_cost = Field('fixedCost')
    fixed_revenue = Field('fixedRevenue')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_notes = Field('hasNotes')
    has_timed_notifications = Field('hasTimedNotifications')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_mode = Field('levelingMode')
    milestone_path_id = Field('milestonePathID')
    name = Field('name')
    olv = Field('olv')
    owner_id = Field('ownerID')
    owner_privileges = Field('ownerPrivileges')
    pending_calculation = Field('pendingCalculation')
    pending_update_methods = Field('pendingUpdateMethods')
    performance_index_method = Field('performanceIndexMethod')
    planned_benefit = Field('plannedBenefit')
    planned_cost = Field('plannedCost')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_risk_cost = Field('plannedRiskCost')
    portfolio_id = Field('portfolioID')
    priority = Field('priority')
    program_id = Field('programID')
    queue_def_id = Field('queueDefID')
    reference_number = Field('referenceNumber')
    risk = Field('risk')
    schedule_id = Field('scheduleID')
    schedule_mode = Field('scheduleMode')
    sponsor_id = Field('sponsorID')
    start_day = Field('startDay')
    summary_completion_type = Field('summaryCompletionType')
    team_id = Field('teamID')
    update_type = Field('updateType')
    version = Field('version')
    work_required = Field('workRequired')
    approval_process = Reference('approvalProcess')
    category = Reference('category')
    company = Reference('company')
    customer = Reference('customer')
    deliverable_score_card = Reference('deliverableScoreCard')
    entered_by = Reference('enteredBy')
    exchange_rate = Reference('exchangeRate')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    milestone_path = Reference('milestonePath')
    owner = Reference('owner')
    portfolio = Reference('portfolio')
    program = Reference('program')
    queue_def = Reference('queueDef')
    schedule = Reference('schedule')
    sharing_settings = Reference('sharingSettings')
    sponsor = Reference('sponsor')
    team = Reference('team')
    access_rule_preferences = Collection('accessRulePreferences')
    access_rules = Collection('accessRules')
    deliverable_values = Collection('deliverableValues')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    expenses = Collection('expenses')
    groups = Collection('groups')
    hour_types = Collection('hourTypes')
    notification_records = Collection('notificationRecords')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')
    rates = Collection('rates')
    risks = Collection('risks')
    roles = Collection('roles')
    routing_rules = Collection('routingRules')
    template_tasks = Collection('templateTasks')
    template_user_roles = Collection('templateUserRoles')
    template_users = Collection('templateUsers')
    updates = Collection('updates')

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def calculate_timeline(self):
        """
        The ``calculateTimeline`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateTimeline', params)
        return data['result']

    def get_template_currency(self):
        """
        The ``getTemplateCurrency`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getTemplateCurrency', params)
        return data['result']

    def remove_users_from_template(self, user_ids=None):
        """
        The ``removeUsersFromTemplate`` action.
        
        :param user_ids: userIDs (type: ``string[]``)
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        data = self.session.put(self.api_url()+'/removeUsersFromTemplate', params)
        

    def set_access_rule_preferences(self, access_rule_preferences=None):
        """
        The ``setAccessRulePreferences`` action.
        
        :param access_rule_preferences: accessRulePreferences (type: ``string[]``)
        """
        params = {}
        if access_rule_preferences is not None: params['accessRulePreferences'] = access_rule_preferences
        data = self.session.put(self.api_url()+'/setAccessRulePreferences', params)
        

api.register(Template)


class TemplateAssignment(Object):
    code = 'TASSGN'
    accessor_ids = Field('accessorIDs')
    assigned_to_id = Field('assignedToID')
    assignment_percent = Field('assignmentPercent')
    customer_id = Field('customerID')
    is_primary = Field('isPrimary')
    is_team_assignment = Field('isTeamAssignment')
    master_task_id = Field('masterTaskID')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    role_id = Field('roleID')
    team_id = Field('teamID')
    template_id = Field('templateID')
    template_task_id = Field('templateTaskID')
    work = Field('work')
    work_required = Field('workRequired')
    work_unit = Field('workUnit')
    assigned_to = Reference('assignedTo')
    customer = Reference('customer')
    master_task = Reference('masterTask')
    role = Reference('role')
    team = Reference('team')
    template = Reference('template')
    template_task = Reference('templateTask')

api.register(TemplateAssignment)


class TemplatePredecessor(Object):
    code = 'TPRED'
    customer_id = Field('customerID')
    is_enforced = Field('isEnforced')
    lag_days = Field('lagDays')
    lag_type = Field('lagType')
    predecessor_id = Field('predecessorID')
    predecessor_type = Field('predecessorType')
    successor_id = Field('successorID')
    customer = Reference('customer')
    predecessor = Reference('predecessor')
    successor = Reference('successor')

api.register(TemplatePredecessor)


class TemplateTask(Object):
    code = 'TTSK'
    url = Field('URL')
    accessor_ids = Field('accessorIDs')
    approval_process_id = Field('approvalProcessID')
    assigned_to_id = Field('assignedToID')
    assignments_list_string = Field('assignmentsListString')
    audit_types = Field('auditTypes')
    billing_amount = Field('billingAmount')
    category_id = Field('categoryID')
    completion_day = Field('completionDay')
    constraint_day = Field('constraintDay')
    cost_amount = Field('costAmount')
    cost_type = Field('costType')
    customer_id = Field('customerID')
    description = Field('description')
    duration = Field('duration')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    duration_type = Field('durationType')
    duration_unit = Field('durationUnit')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_notes = Field('hasNotes')
    has_timed_notifications = Field('hasTimedNotifications')
    indent = Field('indent')
    is_critical = Field('isCritical')
    is_duration_locked = Field('isDurationLocked')
    is_leveling_excluded = Field('isLevelingExcluded')
    is_work_required_locked = Field('isWorkRequiredLocked')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_start_delay = Field('levelingStartDelay')
    leveling_start_delay_minutes = Field('levelingStartDelayMinutes')
    master_task_id = Field('masterTaskID')
    milestone_id = Field('milestoneID')
    name = Field('name')
    number_of_children = Field('numberOfChildren')
    original_duration = Field('originalDuration')
    original_work_required = Field('originalWorkRequired')
    parent_id = Field('parentID')
    parent_lag = Field('parentLag')
    parent_lag_type = Field('parentLagType')
    pending_calculation = Field('pendingCalculation')
    pending_update_methods = Field('pendingUpdateMethods')
    planned_cost = Field('plannedCost')
    planned_duration = Field('plannedDuration')
    planned_duration_minutes = Field('plannedDurationMinutes')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    predecessor_expression = Field('predecessorExpression')
    priority = Field('priority')
    recurrence_number = Field('recurrenceNumber')
    recurrence_rule_id = Field('recurrenceRuleID')
    reference_number = Field('referenceNumber')
    revenue_type = Field('revenueType')
    role_id = Field('roleID')
    start_day = Field('startDay')
    task_constraint = Field('taskConstraint')
    task_number = Field('taskNumber')
    task_number_predecessor_string = Field('taskNumberPredecessorString')
    team_id = Field('teamID')
    template_id = Field('templateID')
    tracking_mode = Field('trackingMode')
    work = Field('work')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    work_unit = Field('workUnit')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    category = Reference('category')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    master_task = Reference('masterTask')
    milestone = Reference('milestone')
    parent = Reference('parent')
    recurrence_rule = Reference('recurrenceRule')
    role = Reference('role')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    template = Reference('template')
    assignments = Collection('assignments')
    children = Collection('children')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    expenses = Collection('expenses')
    notification_records = Collection('notificationRecords')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')
    predecessors = Collection('predecessors')
    successors = Collection('successors')

    def assign_multiple(self, user_ids=None, role_ids=None, team_id=None):
        """
        The ``assignMultiple`` action.
        
        :param user_ids: userIDs (type: ``string[]``)
        :param role_ids: roleIDs (type: ``string[]``)
        :param team_id: teamID (type: ``string``)
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        if role_ids is not None: params['roleIDs'] = role_ids
        if team_id is not None: params['teamID'] = team_id
        data = self.session.put(self.api_url()+'/assignMultiple', params)
        

    def bulk_copy(self, template_id=None, template_task_ids=None, parent_template_task_id=None, options=None):
        """
        The ``bulkCopy`` action.
        
        :param template_id: templateID (type: ``string``)
        :param template_task_ids: templateTaskIDs (type: ``string[]``)
        :param parent_template_task_id: parentTemplateTaskID (type: ``string``)
        :param options: options (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if template_id is not None: params['templateID'] = template_id
        if template_task_ids is not None: params['templateTaskIDs'] = template_task_ids
        if parent_template_task_id is not None: params['parentTemplateTaskID'] = parent_template_task_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/bulkCopy', params)
        return data['result']

    def bulk_move(self, template_task_ids=None, template_id=None, parent_id=None, options=None):
        """
        The ``bulkMove`` action.
        
        :param template_task_ids: templateTaskIDs (type: ``string[]``)
        :param template_id: templateID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        :param options: options (type: ``string[]``)
        :return: ``string``
        """
        params = {}
        if template_task_ids is not None: params['templateTaskIDs'] = template_task_ids
        if template_id is not None: params['templateID'] = template_id
        if parent_id is not None: params['parentID'] = parent_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/bulkMove', params)
        return data['result']

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def move(self, template_id=None, parent_id=None, options=None):
        """
        The ``move`` action.
        
        :param template_id: templateID (type: ``string``)
        :param parent_id: parentID (type: ``string``)
        :param options: options (type: ``string[]``)
        """
        params = {}
        if template_id is not None: params['templateID'] = template_id
        if parent_id is not None: params['parentID'] = parent_id
        if options is not None: params['options'] = options
        data = self.session.put(self.api_url()+'/move', params)
        

    def timed_notifications(self, notification_ids=None):
        """
        The ``timedNotifications`` action.
        
        :param notification_ids: notificationIDs (type: ``string[]``)
        """
        params = {}
        if notification_ids is not None: params['notificationIDs'] = notification_ids
        data = self.session.put(self.api_url()+'/timedNotifications', params)
        

api.register(TemplateTask)


class TemplateUser(Object):
    code = 'TMTU'
    customer_id = Field('customerID')
    template_id = Field('templateID')
    tmp_user_id = Field('tmpUserID')
    user_id = Field('userID')
    customer = Reference('customer')
    template = Reference('template')
    user = Reference('user')

api.register(TemplateUser)


class TemplateUserRole(Object):
    code = 'TTEAM'
    customer_id = Field('customerID')
    role_id = Field('roleID')
    template_id = Field('templateID')
    user_id = Field('userID')
    customer = Reference('customer')
    role = Reference('role')
    template = Reference('template')
    user = Reference('user')

api.register(TemplateUserRole)


class TimedNotification(Object):
    code = 'TMNOT'
    criteria = Field('criteria')
    customer_id = Field('customerID')
    date_field = Field('dateField')
    description = Field('description')
    duration_minutes = Field('durationMinutes')
    duration_unit = Field('durationUnit')
    email_template_id = Field('emailTemplateID')
    name = Field('name')
    recipients = Field('recipients')
    timed_not_obj_code = Field('timedNotObjCode')
    timing = Field('timing')
    customer = Reference('customer')
    email_template = Reference('emailTemplate')

api.register(TimedNotification)


class Timesheet(Object):
    code = 'TSHET'
    approver_can_edit_hours = Field('approverCanEditHours')
    approver_id = Field('approverID')
    approvers_list_string = Field('approversListString')
    available_actions = Field('availableActions')
    customer_id = Field('customerID')
    display_name = Field('displayName')
    end_date = Field('endDate')
    ext_ref_id = Field('extRefID')
    has_notes = Field('hasNotes')
    hours_duration = Field('hoursDuration')
    is_editable = Field('isEditable')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    overtime_hours = Field('overtimeHours')
    regular_hours = Field('regularHours')
    start_date = Field('startDate')
    status = Field('status')
    timesheet_profile_id = Field('timesheetProfileID')
    total_hours = Field('totalHours')
    user_id = Field('userID')
    approver = Reference('approver')
    customer = Reference('customer')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    timesheet_profile = Reference('timesheetProfile')
    user = Reference('user')
    approvers = Collection('approvers')
    awaiting_approvals = Collection('awaitingApprovals')
    hours = Collection('hours')
    notification_records = Collection('notificationRecords')

    def pin_timesheet_object(self, user_id=None, obj_code=None, obj_id=None):
        """
        The ``pinTimesheetObject`` action.
        
        :param user_id: userID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/pinTimesheetObject', params)
        

    def unpin_timesheet_object(self, user_id=None, obj_code=None, obj_id=None):
        """
        The ``unpinTimesheetObject`` action.
        
        :param user_id: userID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        data = self.session.put(self.api_url()+'/unpinTimesheetObject', params)
        

api.register(Timesheet)


class TimesheetProfile(Object):
    code = 'TSPRO'
    period_start_display_name = Field('PeriodStartDisplayName')
    approver_can_edit_hours = Field('approverCanEditHours')
    approver_id = Field('approverID')
    approvers_list_string = Field('approversListString')
    customer_id = Field('customerID')
    description = Field('description')
    effective_end_date = Field('effectiveEndDate')
    effective_start_date = Field('effectiveStartDate')
    entered_by_id = Field('enteredByID')
    is_recurring = Field('isRecurring')
    manager_approval = Field('managerApproval')
    name = Field('name')
    pay_period_type = Field('payPeriodType')
    period_start = Field('periodStart')
    approver = Reference('approver')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    approvers = Collection('approvers')
    hour_types = Collection('hourTypes')
    notification_records = Collection('notificationRecords')

    def generate_customer_timesheets(self, obj_ids=None):
        """
        The ``generateCustomerTimesheets`` action.
        
        :param obj_ids: objIDs (type: ``string[]``)
        """
        params = {}
        if obj_ids is not None: params['objIDs'] = obj_ids
        data = self.session.put(self.api_url()+'/generateCustomerTimesheets', params)
        

    def has_reference(self, ids=None):
        """
        The ``hasReference`` action.
        
        :param ids: ids (type: ``string[]``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/hasReference', params)
        return data['result']

api.register(TimesheetProfile)


class TimesheetTemplate(Object):
    code = 'TSHTMP'
    customer_id = Field('customerID')
    hour_type_id = Field('hourTypeID')
    op_task_id = Field('opTaskID')
    project_id = Field('projectID')
    ref_obj_code = Field('refObjCode')
    ref_obj_id = Field('refObjID')
    task_id = Field('taskID')
    user_id = Field('userID')
    customer = Reference('customer')
    hour_type = Reference('hourType')
    op_task = Reference('opTask')
    project = Reference('project')
    task = Reference('task')
    user = Reference('user')

api.register(TimesheetTemplate)


class UIFilter(Object):
    code = 'UIFT'
    accessor_ids = Field('accessorIDs')
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    definition = Field('definition')
    display_name = Field('displayName')
    entered_by_id = Field('enteredByID')
    filter_type = Field('filterType')
    global_uikey = Field('globalUIKey')
    is_app_global_editable = Field('isAppGlobalEditable')
    is_public = Field('isPublic')
    is_report = Field('isReport')
    is_saved_search = Field('isSavedSearch')
    is_text = Field('isText')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    mod_date = Field('modDate')
    msg_key = Field('msgKey')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    preference_id = Field('preferenceID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    ui_obj_code = Field('uiObjCode')
    app_global = Reference('appGlobal')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    preference = Reference('preference')
    access_rules = Collection('accessRules')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')
    users = Collection('users')

    def un_link_users(self, filter_id=None, linked_user_ids=None):
        """
        The ``unLinkUsers`` action.
        
        :param filter_id: filterID (type: ``string``)
        :param linked_user_ids: linkedUserIDs (type: ``string[]``)
        """
        params = {}
        if filter_id is not None: params['filterID'] = filter_id
        if linked_user_ids is not None: params['linkedUserIDs'] = linked_user_ids
        data = self.session.put(self.api_url()+'/unLinkUsers', params)
        

api.register(UIFilter)


class UIGroupBy(Object):
    code = 'UIGB'
    accessor_ids = Field('accessorIDs')
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    definition = Field('definition')
    display_name = Field('displayName')
    entered_by_id = Field('enteredByID')
    global_uikey = Field('globalUIKey')
    is_app_global_editable = Field('isAppGlobalEditable')
    is_public = Field('isPublic')
    is_report = Field('isReport')
    is_text = Field('isText')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    mod_date = Field('modDate')
    msg_key = Field('msgKey')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    preference_id = Field('preferenceID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    ui_obj_code = Field('uiObjCode')
    app_global = Reference('appGlobal')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    preference = Reference('preference')
    access_rules = Collection('accessRules')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')

    def un_link_users(self, group_id=None, linked_user_ids=None):
        """
        The ``unLinkUsers`` action.
        
        :param group_id: groupID (type: ``string``)
        :param linked_user_ids: linkedUserIDs (type: ``string[]``)
        """
        params = {}
        if group_id is not None: params['groupID'] = group_id
        if linked_user_ids is not None: params['linkedUserIDs'] = linked_user_ids
        data = self.session.put(self.api_url()+'/unLinkUsers', params)
        

api.register(UIGroupBy)


class UIView(Object):
    code = 'UIVW'
    accessor_ids = Field('accessorIDs')
    app_global_id = Field('appGlobalID')
    customer_id = Field('customerID')
    definition = Field('definition')
    display_name = Field('displayName')
    entered_by_id = Field('enteredByID')
    global_uikey = Field('globalUIKey')
    is_app_global_editable = Field('isAppGlobalEditable')
    is_default = Field('isDefault')
    is_new_format = Field('isNewFormat')
    is_public = Field('isPublic')
    is_report = Field('isReport')
    is_text = Field('isText')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    layout_type = Field('layoutType')
    mod_date = Field('modDate')
    msg_key = Field('msgKey')
    name = Field('name')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    preference_id = Field('preferenceID')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    ui_obj_code = Field('uiObjCode')
    uiview_type = Field('uiviewType')
    app_global = Reference('appGlobal')
    customer = Reference('customer')
    entered_by = Reference('enteredBy')
    last_updated_by = Reference('lastUpdatedBy')
    preference = Reference('preference')
    access_rules = Collection('accessRules')
    linked_roles = Collection('linkedRoles')
    linked_teams = Collection('linkedTeams')
    linked_users = Collection('linkedUsers')

    def expand_view_aliases(self, obj_code=None, definition=None):
        """
        The ``expandViewAliases`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param definition: definition (type: ``map``)
        :return: ``map``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if definition is not None: params['definition'] = definition
        data = self.session.put(self.api_url()+'/expandViewAliases', params)
        return data['result']

    def get_view_fields(self):
        """
        The ``getViewFields`` action.
        
        :return: ``string[]``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getViewFields', params)
        return data['result']

    def migrate_uiviews_ppmto_anaconda(self):
        """
        The ``migrateUIViewsPPMToAnaconda`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/migrateUIViewsPPMToAnaconda', params)
        

    def un_link_users(self, view_id=None, linked_user_ids=None):
        """
        The ``unLinkUsers`` action.
        
        :param view_id: viewID (type: ``string``)
        :param linked_user_ids: linkedUserIDs (type: ``string[]``)
        """
        params = {}
        if view_id is not None: params['viewID'] = view_id
        if linked_user_ids is not None: params['linkedUserIDs'] = linked_user_ids
        data = self.session.put(self.api_url()+'/unLinkUsers', params)
        

api.register(UIView)


class Update(Object):
    code = 'UPDATE'
    allowed_actions = Field('allowedActions')
    audit_record_id = Field('auditRecordID')
    entered_by_id = Field('enteredByID')
    entered_by_name = Field('enteredByName')
    entry_date = Field('entryDate')
    icon_name = Field('iconName')
    icon_path = Field('iconPath')
    message = Field('message')
    ref_name = Field('refName')
    ref_obj_code = Field('refObjCode')
    ref_obj_id = Field('refObjID')
    styled_message = Field('styledMessage')
    sub_message = Field('subMessage')
    sub_obj_code = Field('subObjCode')
    sub_obj_id = Field('subObjID')
    thread_id = Field('threadID')
    top_name = Field('topName')
    top_obj_code = Field('topObjCode')
    top_obj_id = Field('topObjID')
    update_actions = Field('updateActions')
    update_obj_code = Field('updateObjCode')
    update_obj_id = Field('updateObjID')
    update_type = Field('updateType')
    audit_record = Reference('auditRecord')
    update_endorsement = Reference('updateEndorsement')
    update_journal_entry = Reference('updateJournalEntry')
    update_note = Reference('updateNote')
    combined_updates = Collection('combinedUpdates')
    message_args = Collection('messageArgs')
    nested_updates = Collection('nestedUpdates')
    replies = Collection('replies')
    sub_message_args = Collection('subMessageArgs')

    def audit_session_count(self, user_id=None, target_user_id=None, start_date=None, end_date=None):
        """
        The ``auditSessionCount`` action.
        
        :param user_id: userID (type: ``string``)
        :param target_user_id: targetUserID (type: ``string``)
        :param start_date: startDate (type: ``dateTime``)
        :param end_date: endDate (type: ``dateTime``)
        :return: ``java.lang.Integer``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if target_user_id is not None: params['targetUserID'] = target_user_id
        if start_date is not None: params['startDate'] = start_date
        if end_date is not None: params['endDate'] = end_date
        data = self.session.put(self.api_url()+'/auditSessionCount', params)
        return data['result']

    def get_update_types_for_stream(self, stream_type=None):
        """
        The ``getUpdateTypesForStream`` action.
        
        :param stream_type: streamType (type: ``string``)
        :return: ``string[]``
        """
        params = {}
        if stream_type is not None: params['streamType'] = stream_type
        data = self.session.put(self.api_url()+'/getUpdateTypesForStream', params)
        return data['result']

    def has_updates_before_date(self, obj_code=None, obj_id=None, date=None):
        """
        The ``hasUpdatesBeforeDate`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :param date: date (type: ``dateTime``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        if date is not None: params['date'] = date
        data = self.session.put(self.api_url()+'/hasUpdatesBeforeDate', params)
        return data['result']

    def is_valid_update_note(self, obj_code=None, obj_id=None, comment_id=None):
        """
        The ``isValidUpdateNote`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param obj_id: objID (type: ``string``)
        :param comment_id: commentID (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if obj_id is not None: params['objID'] = obj_id
        if comment_id is not None: params['commentID'] = comment_id
        data = self.session.put(self.api_url()+'/isValidUpdateNote', params)
        return data['result']

    @property
    def update_obj(self):
        """
        The object referenced by this update.
        """
        return self.session.api.from_data(
            self.session, dict(
                ID=self.update_obj_id,
                objCode=self.update_obj_code
            ))

api.register(Update)


class User(Object):
    code = 'USER'
    access_level_id = Field('accessLevelID')
    address = Field('address')
    address2 = Field('address2')
    avatar_date = Field('avatarDate')
    avatar_download_url = Field('avatarDownloadURL')
    avatar_size = Field('avatarSize')
    avatar_x = Field('avatarX')
    avatar_y = Field('avatarY')
    billing_per_hour = Field('billingPerHour')
    category_id = Field('categoryID')
    city = Field('city')
    company_id = Field('companyID')
    cost_per_hour = Field('costPerHour')
    country = Field('country')
    customer_id = Field('customerID')
    default_hour_type_id = Field('defaultHourTypeID')
    default_interface = Field('defaultInterface')
    delegation_to_id = Field('delegationToID')
    email_addr = Field('emailAddr')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    ext_ref_id = Field('extRefID')
    first_name = Field('firstName')
    fte = Field('fte')
    has_apiaccess = Field('hasAPIAccess')
    has_documents = Field('hasDocuments')
    has_notes = Field('hasNotes')
    has_password = Field('hasPassword')
    has_proof_license = Field('hasProofLicense')
    has_reserved_times = Field('hasReservedTimes')
    home_group_id = Field('homeGroupID')
    home_team_id = Field('homeTeamID')
    is_active = Field('isActive')
    is_admin = Field('isAdmin')
    is_box_authenticated = Field('isBoxAuthenticated')
    is_drop_box_authenticated = Field('isDropBoxAuthenticated')
    is_google_authenticated = Field('isGoogleAuthenticated')
    is_share_point_authenticated = Field('isSharePointAuthenticated')
    is_web_damauthenticated = Field('isWebDAMAuthenticated')
    is_workfront_damauthenticated = Field('isWorkfrontDAMAuthenticated')
    last_entered_note_id = Field('lastEnteredNoteID')
    last_login_date = Field('lastLoginDate')
    last_name = Field('lastName')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    last_whats_new = Field('lastWhatsNew')
    latest_update_note_id = Field('latestUpdateNoteID')
    layout_template_id = Field('layoutTemplateID')
    license_type = Field('licenseType')
    locale = Field('locale')
    login_count = Field('loginCount')
    manager_id = Field('managerID')
    mobile_phone_number = Field('mobilePhoneNumber')
    my_info = Field('myInfo')
    name = Field('name')
    password = Field('password')
    password_date = Field('passwordDate')
    persona = Field('persona')
    phone_extension = Field('phoneExtension')
    phone_number = Field('phoneNumber')
    portal_profile_id = Field('portalProfileID')
    postal_code = Field('postalCode')
    registration_expire_date = Field('registrationExpireDate')
    reset_password_expire_date = Field('resetPasswordExpireDate')
    resource_pool_id = Field('resourcePoolID')
    role_id = Field('roleID')
    schedule_id = Field('scheduleID')
    sso_access_only = Field('ssoAccessOnly')
    sso_username = Field('ssoUsername')
    state = Field('state')
    status_update = Field('statusUpdate')
    time_zone = Field('timeZone')
    timesheet_profile_id = Field('timesheetProfileID')
    title = Field('title')
    username = Field('username')
    web_davprofile = Field('webDAVProfile')
    access_level = Reference('accessLevel')
    category = Reference('category')
    company = Reference('company')
    customer = Reference('customer')
    default_hour_type = Reference('defaultHourType')
    delegation_to = Reference('delegationTo')
    effective_layout_template = Reference('effectiveLayoutTemplate')
    entered_by = Reference('enteredBy')
    external_username = Reference('externalUsername')
    high_priority_work_item = Reference('highPriorityWorkItem')
    home_group = Reference('homeGroup')
    home_team = Reference('homeTeam')
    last_entered_note = Reference('lastEnteredNote')
    last_note = Reference('lastNote')
    last_status_note = Reference('lastStatusNote')
    last_updated_by = Reference('lastUpdatedBy')
    latest_update_note = Reference('latestUpdateNote')
    layout_template = Reference('layoutTemplate')
    manager = Reference('manager')
    portal_profile = Reference('portalProfile')
    resource_pool = Reference('resourcePool')
    role = Reference('role')
    schedule = Reference('schedule')
    timesheet_profile = Reference('timesheetProfile')
    access_rule_preferences = Collection('accessRulePreferences')
    custom_tabs = Collection('customTabs')
    delegations_from = Collection('delegationsFrom')
    direct_reports = Collection('directReports')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    external_sections = Collection('externalSections')
    favorites = Collection('favorites')
    hour_types = Collection('hourTypes')
    linked_portal_tabs = Collection('linkedPortalTabs')
    messages = Collection('messages')
    mobile_devices = Collection('mobileDevices')
    object_categories = Collection('objectCategories')
    parameter_values = Collection('parameterValues')
    portal_sections = Collection('portalSections')
    portal_tabs = Collection('portalTabs')
    reserved_times = Collection('reservedTimes')
    roles = Collection('roles')
    teams = Collection('teams')
    timesheet_templates = Collection('timesheetTemplates')
    ui_filters = Collection('uiFilters')
    ui_group_bys = Collection('uiGroupBys')
    ui_views = Collection('uiViews')
    updates = Collection('updates')
    user_activities = Collection('userActivities')
    user_groups = Collection('userGroups')
    user_pref_values = Collection('userPrefValues')
    watch_list = Collection('watchList')
    work_items = Collection('workItems')

    def add_customer_feedback_improvement(self, is_better=None, comment=None):
        """
        The ``addCustomerFeedbackImprovement`` action.
        
        :param is_better: isBetter (type: ``boolean``)
        :param comment: comment (type: ``string``)
        """
        params = {}
        if is_better is not None: params['isBetter'] = is_better
        if comment is not None: params['comment'] = comment
        data = self.session.put(self.api_url()+'/addCustomerFeedbackImprovement', params)
        

    def add_customer_feedback_score_rating(self, score=None, comment=None):
        """
        The ``addCustomerFeedbackScoreRating`` action.
        
        :param score: score (type: ``int``)
        :param comment: comment (type: ``string``)
        """
        params = {}
        if score is not None: params['score'] = score
        if comment is not None: params['comment'] = comment
        data = self.session.put(self.api_url()+'/addCustomerFeedbackScoreRating', params)
        

    def add_early_access(self, ids=None):
        """
        The ``addEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/addEarlyAccess', params)
        

    def add_external_user(self, email_addr=None):
        """
        The ``addExternalUser`` action.
        
        :param email_addr: emailAddr (type: ``string``)
        :return: ``string``
        """
        params = {}
        if email_addr is not None: params['emailAddr'] = email_addr
        data = self.session.put(self.api_url()+'/addExternalUser', params)
        return data['result']

    def add_mobile_device(self, token=None, device_type=None):
        """
        The ``addMobileDevice`` action.
        
        :param token: token (type: ``string``)
        :param device_type: deviceType (type: ``string``)
        :return: ``map``
        """
        params = {}
        if token is not None: params['token'] = token
        if device_type is not None: params['deviceType'] = device_type
        data = self.session.put(self.api_url()+'/addMobileDevice', params)
        return data['result']

    def assign_user_token(self):
        """
        The ``assignUserToken`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/assignUserToken', params)
        return data['result']

    def calculate_data_extension(self):
        """
        The ``calculateDataExtension`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/calculateDataExtension', params)
        

    def check_other_user_early_access(self):
        """
        The ``checkOtherUserEarlyAccess`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/checkOtherUserEarlyAccess', params)
        return data['result']

    def clear_access_rule_preferences(self, obj_code=None):
        """
        The ``clearAccessRulePreferences`` action.
        
        :param obj_code: objCode (type: ``string``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        data = self.session.put(self.api_url()+'/clearAccessRulePreferences', params)
        

    def clear_api_key(self):
        """
        The ``clearApiKey`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/clearApiKey', params)
        return data['result']

    def complete_external_user_registration(self, first_name=None, last_name=None, new_password=None):
        """
        The ``completeExternalUserRegistration`` action.
        
        :param first_name: firstName (type: ``string``)
        :param last_name: lastName (type: ``string``)
        :param new_password: newPassword (type: ``string``)
        """
        params = {}
        if first_name is not None: params['firstName'] = first_name
        if last_name is not None: params['lastName'] = last_name
        if new_password is not None: params['newPassword'] = new_password
        data = self.session.put(self.api_url()+'/completeExternalUserRegistration', params)
        

    def complete_user_registration(self, first_name=None, last_name=None, token=None, title=None, new_password=None):
        """
        The ``completeUserRegistration`` action.
        
        :param first_name: firstName (type: ``string``)
        :param last_name: lastName (type: ``string``)
        :param token: token (type: ``string``)
        :param title: title (type: ``string``)
        :param new_password: newPassword (type: ``string``)
        """
        params = {}
        if first_name is not None: params['firstName'] = first_name
        if last_name is not None: params['lastName'] = last_name
        if token is not None: params['token'] = token
        if title is not None: params['title'] = title
        if new_password is not None: params['newPassword'] = new_password
        data = self.session.put(self.api_url()+'/completeUserRegistration', params)
        

    def delete_early_access(self, ids=None):
        """
        The ``deleteEarlyAccess`` action.
        
        :param ids: ids (type: ``string[]``)
        """
        params = {}
        if ids is not None: params['ids'] = ids
        data = self.session.put(self.api_url()+'/deleteEarlyAccess', params)
        

    def expire_password(self):
        """
        The ``expirePassword`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/expirePassword', params)
        

    def get_api_key(self):
        """
        The ``getApiKey`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getApiKey', params)
        return data['result']

    def get_next_customer_feedback_type(self):
        """
        The ``getNextCustomerFeedbackType`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getNextCustomerFeedbackType', params)
        return data['result']

    def get_or_add_external_user(self, email_addr=None):
        """
        The ``getOrAddExternalUser`` action.
        
        :param email_addr: emailAddr (type: ``string``)
        :return: ``string``
        """
        params = {}
        if email_addr is not None: params['emailAddr'] = email_addr
        data = self.session.put(self.api_url()+'/getOrAddExternalUser', params)
        return data['result']

    def get_reset_password_token_expired(self, token=None):
        """
        The ``getResetPasswordTokenExpired`` action.
        
        :param token: token (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if token is not None: params['token'] = token
        data = self.session.put(self.api_url()+'/getResetPasswordTokenExpired', params)
        return data['result']

    def has_early_access(self):
        """
        The ``hasEarlyAccess`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/hasEarlyAccess', params)
        return data['result']

    def is_npssurvey_available(self):
        """
        The ``isNPSSurveyAvailable`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/isNPSSurveyAvailable', params)
        return data['result']

    def is_username_re_captcha_required(self):
        """
        The ``isUsernameReCaptchaRequired`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/isUsernameReCaptchaRequired', params)
        return data['result']

    def migrate_users_ppmto_anaconda(self):
        """
        The ``migrateUsersPPMToAnaconda`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/migrateUsersPPMToAnaconda', params)
        

    def remove_mobile_device(self, token=None):
        """
        The ``removeMobileDevice`` action.
        
        :param token: token (type: ``string``)
        :return: ``map``
        """
        params = {}
        if token is not None: params['token'] = token
        data = self.session.put(self.api_url()+'/removeMobileDevice', params)
        return data['result']

    def reset_password(self, old_password=None, new_password=None):
        """
        The ``resetPassword`` action.
        
        :param old_password: oldPassword (type: ``string``)
        :param new_password: newPassword (type: ``string``)
        """
        params = {}
        if old_password is not None: params['oldPassword'] = old_password
        if new_password is not None: params['newPassword'] = new_password
        data = self.session.put(self.api_url()+'/resetPassword', params)
        

    def retrieve_and_store_oauth2tokens(self, state=None, authorization_code=None):
        """
        The ``retrieveAndStoreOAuth2Tokens`` action.
        
        :param state: state (type: ``string``)
        :param authorization_code: authorizationCode (type: ``string``)
        """
        params = {}
        if state is not None: params['state'] = state
        if authorization_code is not None: params['authorizationCode'] = authorization_code
        data = self.session.put(self.api_url()+'/retrieveAndStoreOAuth2Tokens', params)
        

    def retrieve_and_store_oauth_token(self, oauth_token=None):
        """
        The ``retrieveAndStoreOAuthToken`` action.
        
        :param oauth_token: oauth_token (type: ``string``)
        """
        params = {}
        if oauth_token is not None: params['oauth_token'] = oauth_token
        data = self.session.put(self.api_url()+'/retrieveAndStoreOAuthToken', params)
        

    def send_invitation_email(self):
        """
        The ``sendInvitationEmail`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/sendInvitationEmail', params)
        

    def set_access_rule_preferences(self, access_rule_preferences=None):
        """
        The ``setAccessRulePreferences`` action.
        
        :param access_rule_preferences: accessRulePreferences (type: ``string[]``)
        """
        params = {}
        if access_rule_preferences is not None: params['accessRulePreferences'] = access_rule_preferences
        data = self.session.put(self.api_url()+'/setAccessRulePreferences', params)
        

    def submit_npssurvey(self, data_map=None):
        """
        The ``submitNPSSurvey`` action.
        
        :param data_map: dataMap (type: ``map``)
        """
        params = {}
        if data_map is not None: params['dataMap'] = data_map
        data = self.session.put(self.api_url()+'/submitNPSSurvey', params)
        

    def update_next_survey_on_date(self, next_suvey_date=None):
        """
        The ``updateNextSurveyOnDate`` action.
        
        :param next_suvey_date: nextSuveyDate (type: ``dateTime``)
        """
        params = {}
        if next_suvey_date is not None: params['nextSuveyDate'] = next_suvey_date
        data = self.session.put(self.api_url()+'/updateNextSurveyOnDate', params)
        

    def validate_re_captcha(self, captcha_response=None):
        """
        The ``validateReCaptcha`` action.
        
        :param captcha_response: captchaResponse (type: ``string``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if captcha_response is not None: params['captchaResponse'] = captcha_response
        data = self.session.put(self.api_url()+'/validateReCaptcha', params)
        return data['result']

api.register(User)


class UserActivity(Object):
    code = 'USERAC'
    customer_id = Field('customerID')
    entry_date = Field('entryDate')
    last_update_date = Field('lastUpdateDate')
    name = Field('name')
    user_id = Field('userID')
    value = Field('value')
    customer = Reference('customer')
    user = Reference('user')

api.register(UserActivity)


class UserAvailability(Object):
    code = 'USRAVL'
    availability_date = Field('availabilityDate')
    customer_id = Field('customerID')
    olv = Field('olv')
    planned_allocation_percent = Field('plannedAllocationPercent')
    planned_assigned_minutes = Field('plannedAssignedMinutes')
    planned_remaining_minutes = Field('plannedRemainingMinutes')
    projected_allocation_percent = Field('projectedAllocationPercent')
    projected_assigned_minutes = Field('projectedAssignedMinutes')
    projected_remaining_minutes = Field('projectedRemainingMinutes')
    total_minutes = Field('totalMinutes')
    user_id = Field('userID')
    customer = Reference('customer')
    user = Reference('user')

    def delete_duplicate_availability(self, duplicate_user_availability_ids=None):
        """
        The ``deleteDuplicateAvailability`` action.
        
        :param duplicate_user_availability_ids: duplicateUserAvailabilityIDs (type: ``string[]``)
        """
        params = {}
        if duplicate_user_availability_ids is not None: params['duplicateUserAvailabilityIDs'] = duplicate_user_availability_ids
        data = self.session.put(self.api_url()+'/deleteDuplicateAvailability', params)
        

    def get_user_assignments(self, user_id=None, start_date=None, end_date=None):
        """
        The ``getUserAssignments`` action.
        
        :param user_id: userID (type: ``string``)
        :param start_date: startDate (type: ``string``)
        :param end_date: endDate (type: ``string``)
        :return: ``string[]``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if start_date is not None: params['startDate'] = start_date
        if end_date is not None: params['endDate'] = end_date
        data = self.session.put(self.api_url()+'/getUserAssignments', params)
        return data['result']

api.register(UserAvailability)


class UserDelegation(Object):
    code = 'USRDEL'
    customer_id = Field('customerID')
    end_date = Field('endDate')
    from_user_id = Field('fromUserID')
    start_date = Field('startDate')
    to_user_id = Field('toUserID')
    customer = Reference('customer')
    from_user = Reference('fromUser')
    to_user = Reference('toUser')

api.register(UserDelegation)


class UserGroups(Object):
    code = 'USRGPS'
    customer_id = Field('customerID')
    group_id = Field('groupID')
    is_owner = Field('isOwner')
    user_id = Field('userID')
    customer = Reference('customer')
    group = Reference('group')
    user = Reference('user')

api.register(UserGroups)


class UserNote(Object):
    code = 'USRNOT'
    acknowledgement_id = Field('acknowledgementID')
    announcement_favorite_id = Field('announcementFavoriteID')
    announcement_id = Field('announcementID')
    customer_id = Field('customerID')
    document_approval_id = Field('documentApprovalID')
    document_request_id = Field('documentRequestID')
    document_share_id = Field('documentShareID')
    endorsement_id = Field('endorsementID')
    endorsement_share_id = Field('endorsementShareID')
    entry_date = Field('entryDate')
    event_type = Field('eventType')
    journal_entry_id = Field('journalEntryID')
    like_id = Field('likeID')
    marked_deleted_date = Field('markedDeletedDate')
    note_id = Field('noteID')
    user_id = Field('userID')
    user_notable_id = Field('userNotableID')
    user_notable_obj_code = Field('userNotableObjCode')
    acknowledgement = Reference('acknowledgement')
    announcement = Reference('announcement')
    customer = Reference('customer')
    document_approval = Reference('documentApproval')
    document_request = Reference('documentRequest')
    document_share = Reference('documentShare')
    endorsement = Reference('endorsement')
    endorsement_share = Reference('endorsementShare')
    journal_entry = Reference('journalEntry')
    like = Reference('like')
    note = Reference('note')
    user = Reference('user')

    def acknowledge(self):
        """
        The ``acknowledge`` action.
        
        :return: ``string``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/acknowledge', params)
        return data['result']

    def acknowledge_all(self):
        """
        The ``acknowledgeAll`` action.
        
        :return: ``string[]``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/acknowledgeAll', params)
        return data['result']

    def acknowledge_many(self, obj_ids=None):
        """
        The ``acknowledgeMany`` action.
        
        :param obj_ids: objIDs (type: ``string[]``)
        :return: ``string[]``
        """
        params = {}
        if obj_ids is not None: params['objIDs'] = obj_ids
        data = self.session.put(self.api_url()+'/acknowledgeMany', params)
        return data['result']

    def add_team_note(self, team_id=None, obj_code=None, target_id=None, type=None):
        """
        The ``addTeamNote`` action.
        
        :param team_id: teamID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param target_id: targetID (type: ``string``)
        :param type: type (type: ``com.attask.common.constants.UserNoteEventEnum``)
        :return: ``java.util.Collection``
        """
        params = {}
        if team_id is not None: params['teamID'] = team_id
        if obj_code is not None: params['objCode'] = obj_code
        if target_id is not None: params['targetID'] = target_id
        if type is not None: params['type'] = type
        data = self.session.put(self.api_url()+'/addTeamNote', params)
        return data['result']

    def add_teams_notes(self, team_ids=None, obj_code=None, target_id=None, type=None):
        """
        The ``addTeamsNotes`` action.
        
        :param team_ids: teamIDs (type: ``java.util.Collection``)
        :param obj_code: objCode (type: ``string``)
        :param target_id: targetID (type: ``string``)
        :param type: type (type: ``com.attask.common.constants.UserNoteEventEnum``)
        :return: ``java.util.Collection``
        """
        params = {}
        if team_ids is not None: params['teamIDs'] = team_ids
        if obj_code is not None: params['objCode'] = obj_code
        if target_id is not None: params['targetID'] = target_id
        if type is not None: params['type'] = type
        data = self.session.put(self.api_url()+'/addTeamsNotes', params)
        return data['result']

    def add_user_note(self, user_id=None, obj_code=None, target_id=None, type=None):
        """
        The ``addUserNote`` action.
        
        :param user_id: userID (type: ``string``)
        :param obj_code: objCode (type: ``string``)
        :param target_id: targetID (type: ``string``)
        :param type: type (type: ``com.attask.common.constants.UserNoteEventEnum``)
        :return: ``string``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if obj_code is not None: params['objCode'] = obj_code
        if target_id is not None: params['targetID'] = target_id
        if type is not None: params['type'] = type
        data = self.session.put(self.api_url()+'/addUserNote', params)
        return data['result']

    def add_users_notes(self, user_ids=None, obj_code=None, target_id=None, type=None):
        """
        The ``addUsersNotes`` action.
        
        :param user_ids: userIDs (type: ``java.util.Collection``)
        :param obj_code: objCode (type: ``string``)
        :param target_id: targetID (type: ``string``)
        :param type: type (type: ``com.attask.common.constants.UserNoteEventEnum``)
        :return: ``java.util.Collection``
        """
        params = {}
        if user_ids is not None: params['userIDs'] = user_ids
        if obj_code is not None: params['objCode'] = obj_code
        if target_id is not None: params['targetID'] = target_id
        if type is not None: params['type'] = type
        data = self.session.put(self.api_url()+'/addUsersNotes', params)
        return data['result']

    def get_my_notification_last_view_date(self):
        """
        The ``getMyNotificationLastViewDate`` action.
        
        :return: ``dateTime``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getMyNotificationLastViewDate', params)
        return data['result']

    def has_announcement_delete_access(self):
        """
        The ``hasAnnouncementDeleteAccess`` action.
        
        :return: ``java.lang.Boolean``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/hasAnnouncementDeleteAccess', params)
        return data['result']

    def mark_deleted(self, note_id=None):
        """
        The ``markDeleted`` action.
        
        :param note_id: noteID (type: ``string``)
        """
        params = {}
        if note_id is not None: params['noteID'] = note_id
        data = self.session.put(self.api_url()+'/markDeleted', params)
        

    def unacknowledge(self):
        """
        The ``unacknowledge`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unacknowledge', params)
        

    def unacknowledged_announcement_count(self):
        """
        The ``unacknowledgedAnnouncementCount`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unacknowledgedAnnouncementCount', params)
        return data['result']

    def unacknowledged_count(self):
        """
        The ``unacknowledgedCount`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/unacknowledgedCount', params)
        return data['result']

    def unmark_deleted(self, note_id=None):
        """
        The ``unmarkDeleted`` action.
        
        :param note_id: noteID (type: ``string``)
        """
        params = {}
        if note_id is not None: params['noteID'] = note_id
        data = self.session.put(self.api_url()+'/unmarkDeleted', params)
        

api.register(UserNote)


class UserObjectPref(Object):
    code = 'USOP'
    customer_id = Field('customerID')
    last_update_date = Field('lastUpdateDate')
    name = Field('name')
    ref_obj_code = Field('refObjCode')
    ref_obj_id = Field('refObjID')
    user_id = Field('userID')
    value = Field('value')
    customer = Reference('customer')
    user = Reference('user')

    def set(self, user_id=None, ref_obj_code=None, ref_obj_id=None, name=None, value=None):
        """
        The ``set`` action.
        
        :param user_id: userID (type: ``string``)
        :param ref_obj_code: refObjCode (type: ``string``)
        :param ref_obj_id: refObjID (type: ``string``)
        :param name: name (type: ``string``)
        :param value: value (type: ``string``)
        :return: ``string``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if ref_obj_code is not None: params['refObjCode'] = ref_obj_code
        if ref_obj_id is not None: params['refObjID'] = ref_obj_id
        if name is not None: params['name'] = name
        if value is not None: params['value'] = value
        data = self.session.put(self.api_url()+'/set', params)
        return data['result']

api.register(UserObjectPref)


class UserPrefValue(Object):
    code = 'USERPF'
    customer_id = Field('customerID')
    name = Field('name')
    user_id = Field('userID')
    value = Field('value')
    customer = Reference('customer')
    user = Reference('user')

    def get_inactive_notifications_value(self, user_id=None):
        """
        The ``getInactiveNotificationsValue`` action.
        
        :param user_id: userID (type: ``string``)
        :return: ``string``
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/getInactiveNotificationsValue', params)
        return data['result']

    def set_inactive_notifications_value(self, user_id=None, value=None):
        """
        The ``setInactiveNotificationsValue`` action.
        
        :param user_id: userID (type: ``string``)
        :param value: value (type: ``string``)
        """
        params = {}
        if user_id is not None: params['userID'] = user_id
        if value is not None: params['value'] = value
        data = self.session.put(self.api_url()+'/setInactiveNotificationsValue', params)
        

api.register(UserPrefValue)


class UserResource(Object):
    code = 'USERRS'
    actual_allocation_percentage = Field('actualAllocationPercentage')
    actual_day_summaries = Field('actualDaySummaries')
    allocation_percentage = Field('allocationPercentage')
    allowed_actions = Field('allowedActions')
    available_number_of_hours = Field('availableNumberOfHours')
    available_time_per_day = Field('availableTimePerDay')
    average_actual_number_of_hours = Field('averageActualNumberOfHours')
    average_number_of_hours = Field('averageNumberOfHours')
    average_projected_number_of_hours = Field('averageProjectedNumberOfHours')
    day_summaries = Field('daySummaries')
    detail_level = Field('detailLevel')
    number_of_assignments = Field('numberOfAssignments')
    number_of_days_within_actual_threshold = Field('numberOfDaysWithinActualThreshold')
    number_of_days_within_projected_threshold = Field('numberOfDaysWithinProjectedThreshold')
    number_of_days_within_threshold = Field('numberOfDaysWithinThreshold')
    obj_code = Field('objCode')
    projected_allocation_percentage = Field('projectedAllocationPercentage')
    projected_day_summaries = Field('projectedDaySummaries')
    total_actual_hours = Field('totalActualHours')
    total_available_hours = Field('totalAvailableHours')
    total_number_of_hours = Field('totalNumberOfHours')
    total_projected_hours = Field('totalProjectedHours')
    working_days = Field('workingDays')
    role = Reference('role')
    user = Reference('user')
    user_home_team = Reference('userHomeTeam')
    user_primary_role = Reference('userPrimaryRole')
    assignments = Collection('assignments')

api.register(UserResource)


class UsersSections(Object):
    code = 'USRSEC'
    customer_id = Field('customerID')
    section_id = Field('sectionID')
    user_id = Field('userID')

api.register(UsersSections)


class WatchListEntry(Object):
    code = 'WATCH'
    customer_id = Field('customerID')
    optask_id = Field('optaskID')
    project_id = Field('projectID')
    task_id = Field('taskID')
    user_id = Field('userID')
    watchable_obj_code = Field('watchableObjCode')
    watchable_obj_id = Field('watchableObjID')
    customer = Reference('customer')
    optask = Reference('optask')
    project = Reference('project')
    task = Reference('task')
    user = Reference('user')

api.register(WatchListEntry)


class WhatsNew(Object):
    code = 'WTSN'
    description = Field('description')
    entry_date = Field('entryDate')
    feature_name = Field('featureName')
    locale = Field('locale')
    product_toggle = Field('productToggle')
    start_date = Field('startDate')
    title = Field('title')
    whats_new_types = Field('whatsNewTypes')

    def is_whats_new_available(self, product_toggle=None):
        """
        The ``isWhatsNewAvailable`` action.
        
        :param product_toggle: productToggle (type: ``int``)
        :return: ``java.lang.Boolean``
        """
        params = {}
        if product_toggle is not None: params['productToggle'] = product_toggle
        data = self.session.put(self.api_url()+'/isWhatsNewAvailable', params)
        return data['result']

api.register(WhatsNew)


class Work(Object):
    code = 'WORK'
    url = Field('URL')
    accessor_ids = Field('accessorIDs')
    actual_completion_date = Field('actualCompletionDate')
    actual_cost = Field('actualCost')
    actual_duration = Field('actualDuration')
    actual_duration_minutes = Field('actualDurationMinutes')
    actual_expense_cost = Field('actualExpenseCost')
    actual_labor_cost = Field('actualLaborCost')
    actual_revenue = Field('actualRevenue')
    actual_start_date = Field('actualStartDate')
    actual_work = Field('actualWork')
    actual_work_required = Field('actualWorkRequired')
    actual_work_required_expression = Field('actualWorkRequiredExpression')
    age_range_as_string = Field('ageRangeAsString')
    approval_est_start_date = Field('approvalEstStartDate')
    approval_planned_start_date = Field('approvalPlannedStartDate')
    approval_planned_start_day = Field('approvalPlannedStartDay')
    approval_process_id = Field('approvalProcessID')
    approval_projected_start_date = Field('approvalProjectedStartDate')
    approvers_string = Field('approversString')
    assigned_to_id = Field('assignedToID')
    assignments_list_string = Field('assignmentsListString')
    audit_note = Field('auditNote')
    audit_types = Field('auditTypes')
    audit_user_ids = Field('auditUserIDs')
    auto_closure_date = Field('autoClosureDate')
    backlog_order = Field('backlogOrder')
    billing_amount = Field('billingAmount')
    billing_record_id = Field('billingRecordID')
    can_start = Field('canStart')
    category_id = Field('categoryID')
    color = Field('color')
    commit_date = Field('commitDate')
    commit_date_range = Field('commitDateRange')
    completion_pending_date = Field('completionPendingDate')
    condition = Field('condition')
    constraint_date = Field('constraintDate')
    converted_op_task_entry_date = Field('convertedOpTaskEntryDate')
    converted_op_task_name = Field('convertedOpTaskName')
    converted_op_task_originator_id = Field('convertedOpTaskOriginatorID')
    cost_amount = Field('costAmount')
    cost_type = Field('costType')
    cpi = Field('cpi')
    csi = Field('csi')
    current_approval_step_id = Field('currentApprovalStepID')
    current_status_duration = Field('currentStatusDuration')
    customer_id = Field('customerID')
    days_late = Field('daysLate')
    description = Field('description')
    display_queue_breadcrumb = Field('displayQueueBreadcrumb')
    due_date = Field('dueDate')
    duration = Field('duration')
    duration_expression = Field('durationExpression')
    duration_minutes = Field('durationMinutes')
    duration_type = Field('durationType')
    duration_unit = Field('durationUnit')
    eac = Field('eac')
    entered_by_id = Field('enteredByID')
    entry_date = Field('entryDate')
    est_completion_date = Field('estCompletionDate')
    est_start_date = Field('estStartDate')
    estimate = Field('estimate')
    ext_ref_id = Field('extRefID')
    first_response = Field('firstResponse')
    group_id = Field('groupID')
    handoff_date = Field('handoffDate')
    has_completion_constraint = Field('hasCompletionConstraint')
    has_documents = Field('hasDocuments')
    has_expenses = Field('hasExpenses')
    has_messages = Field('hasMessages')
    has_notes = Field('hasNotes')
    has_resolvables = Field('hasResolvables')
    has_start_constraint = Field('hasStartConstraint')
    has_timed_notifications = Field('hasTimedNotifications')
    hours_per_point = Field('hoursPerPoint')
    how_old = Field('howOld')
    indent = Field('indent')
    is_agile = Field('isAgile')
    is_complete = Field('isComplete')
    is_critical = Field('isCritical')
    is_duration_locked = Field('isDurationLocked')
    is_help_desk = Field('isHelpDesk')
    is_leveling_excluded = Field('isLevelingExcluded')
    is_ready = Field('isReady')
    is_status_complete = Field('isStatusComplete')
    is_work_required_locked = Field('isWorkRequiredLocked')
    iteration_id = Field('iterationID')
    last_condition_note_id = Field('lastConditionNoteID')
    last_note_id = Field('lastNoteID')
    last_update_date = Field('lastUpdateDate')
    last_updated_by_id = Field('lastUpdatedByID')
    leveling_start_delay = Field('levelingStartDelay')
    leveling_start_delay_expression = Field('levelingStartDelayExpression')
    leveling_start_delay_minutes = Field('levelingStartDelayMinutes')
    master_task_id = Field('masterTaskID')
    milestone_id = Field('milestoneID')
    name = Field('name')
    number_of_children = Field('numberOfChildren')
    number_open_op_tasks = Field('numberOpenOpTasks')
    olv = Field('olv')
    op_task_type = Field('opTaskType')
    op_task_type_label = Field('opTaskTypeLabel')
    original_duration = Field('originalDuration')
    original_work_required = Field('originalWorkRequired')
    owner_id = Field('ownerID')
    parent_id = Field('parentID')
    parent_lag = Field('parentLag')
    parent_lag_type = Field('parentLagType')
    pending_calculation = Field('pendingCalculation')
    pending_predecessors = Field('pendingPredecessors')
    pending_update_methods = Field('pendingUpdateMethods')
    percent_complete = Field('percentComplete')
    personal = Field('personal')
    planned_completion_date = Field('plannedCompletionDate')
    planned_cost = Field('plannedCost')
    planned_date_alignment = Field('plannedDateAlignment')
    planned_duration = Field('plannedDuration')
    planned_duration_minutes = Field('plannedDurationMinutes')
    planned_expense_cost = Field('plannedExpenseCost')
    planned_hours_alignment = Field('plannedHoursAlignment')
    planned_labor_cost = Field('plannedLaborCost')
    planned_revenue = Field('plannedRevenue')
    planned_start_date = Field('plannedStartDate')
    predecessor_expression = Field('predecessorExpression')
    previous_status = Field('previousStatus')
    priority = Field('priority')
    progress_status = Field('progressStatus')
    project_id = Field('projectID')
    projected_completion_date = Field('projectedCompletionDate')
    projected_duration_minutes = Field('projectedDurationMinutes')
    projected_start_date = Field('projectedStartDate')
    queue_topic_breadcrumb = Field('queueTopicBreadcrumb')
    queue_topic_id = Field('queueTopicID')
    recurrence_number = Field('recurrenceNumber')
    recurrence_rule_id = Field('recurrenceRuleID')
    reference_number = Field('referenceNumber')
    reference_obj_code = Field('referenceObjCode')
    reference_obj_id = Field('referenceObjID')
    rejection_issue_id = Field('rejectionIssueID')
    remaining_duration_minutes = Field('remainingDurationMinutes')
    reserved_time_id = Field('reservedTimeID')
    resolution_time = Field('resolutionTime')
    resolve_op_task_id = Field('resolveOpTaskID')
    resolve_project_id = Field('resolveProjectID')
    resolve_task_id = Field('resolveTaskID')
    resolving_obj_code = Field('resolvingObjCode')
    resolving_obj_id = Field('resolvingObjID')
    resource_scope = Field('resourceScope')
    revenue_type = Field('revenueType')
    role_id = Field('roleID')
    security_ancestors_disabled = Field('securityAncestorsDisabled')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    severity = Field('severity')
    show_commit_date = Field('showCommitDate')
    show_condition = Field('showCondition')
    show_status = Field('showStatus')
    slack_date = Field('slackDate')
    source_obj_code = Field('sourceObjCode')
    source_obj_id = Field('sourceObjID')
    source_task_id = Field('sourceTaskID')
    spi = Field('spi')
    status = Field('status')
    status_equates_with = Field('statusEquatesWith')
    status_update = Field('statusUpdate')
    submitted_by_id = Field('submittedByID')
    task_constraint = Field('taskConstraint')
    task_number = Field('taskNumber')
    task_number_predecessor_string = Field('taskNumberPredecessorString')
    team_id = Field('teamID')
    template_task_id = Field('templateTaskID')
    tracking_mode = Field('trackingMode')
    url_ = Field('url')
    version = Field('version')
    wbs = Field('wbs')
    work = Field('work')
    work_required = Field('workRequired')
    work_required_expression = Field('workRequiredExpression')
    work_unit = Field('workUnit')
    approval_process = Reference('approvalProcess')
    assigned_to = Reference('assignedTo')
    billing_record = Reference('billingRecord')
    category = Reference('category')
    converted_op_task_originator = Reference('convertedOpTaskOriginator')
    current_approval_step = Reference('currentApprovalStep')
    customer = Reference('customer')
    default_baseline_task = Reference('defaultBaselineTask')
    entered_by = Reference('enteredBy')
    group = Reference('group')
    iteration = Reference('iteration')
    last_condition_note = Reference('lastConditionNote')
    last_note = Reference('lastNote')
    last_updated_by = Reference('lastUpdatedBy')
    master_task = Reference('masterTask')
    milestone = Reference('milestone')
    owner = Reference('owner')
    parent = Reference('parent')
    primary_assignment = Reference('primaryAssignment')
    project = Reference('project')
    queue_topic = Reference('queueTopic')
    recurrence_rule = Reference('recurrenceRule')
    rejection_issue = Reference('rejectionIssue')
    reserved_time = Reference('reservedTime')
    resolve_op_task = Reference('resolveOpTask')
    resolve_project = Reference('resolveProject')
    resolve_task = Reference('resolveTask')
    role = Reference('role')
    source_task = Reference('sourceTask')
    submitted_by = Reference('submittedBy')
    team = Reference('team')
    team_assignment = Reference('teamAssignment')
    template_task = Reference('templateTask')
    work_item = Reference('workItem')
    access_rules = Collection('accessRules')
    all_priorities = Collection('allPriorities')
    all_severities = Collection('allSeverities')
    all_statuses = Collection('allStatuses')
    approver_statuses = Collection('approverStatuses')
    assignments = Collection('assignments')
    awaiting_approvals = Collection('awaitingApprovals')
    children = Collection('children')
    document_requests = Collection('documentRequests')
    documents = Collection('documents')
    done_statuses = Collection('doneStatuses')
    expenses = Collection('expenses')
    hours = Collection('hours')
    notification_records = Collection('notificationRecords')
    object_categories = Collection('objectCategories')
    op_tasks = Collection('opTasks')
    open_op_tasks = Collection('openOpTasks')
    parameter_values = Collection('parameterValues')
    predecessors = Collection('predecessors')
    resolvables = Collection('resolvables')
    security_ancestors = Collection('securityAncestors')
    successors = Collection('successors')
    updates = Collection('updates')

    def get_my_accomplishments_count(self):
        """
        The ``getMyAccomplishmentsCount`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getMyAccomplishmentsCount', params)
        return data['result']

    def get_my_work_count(self):
        """
        The ``getMyWorkCount`` action.
        
        :return: ``java.lang.Integer``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/getMyWorkCount', params)
        return data['result']

    def get_work_requests_count(self, filters=None):
        """
        The ``getWorkRequestsCount`` action.
        
        :param filters: filters (type: ``map``)
        :return: ``java.lang.Integer``
        """
        params = {}
        if filters is not None: params['filters'] = filters
        data = self.session.put(self.api_url()+'/getWorkRequestsCount', params)
        return data['result']

    def team_request_count(self, filters=None):
        """
        The ``teamRequestCount`` action.
        
        :param filters: filters (type: ``map``)
        :return: ``java.lang.Integer``
        """
        params = {}
        if filters is not None: params['filters'] = filters
        data = self.session.put(self.api_url()+'/teamRequestCount', params)
        return data['result']

    def team_requests_count(self):
        """
        The ``teamRequestsCount`` action.
        
        :return: ``map``
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/teamRequestsCount', params)
        return data['result']

api.register(Work)


class WorkItem(Object):
    code = 'WRKITM'
    accessor_ids = Field('accessorIDs')
    assignment_id = Field('assignmentID')
    customer_id = Field('customerID')
    done_date = Field('doneDate')
    ext_ref_id = Field('extRefID')
    is_dead = Field('isDead')
    is_done = Field('isDone')
    last_viewed_date = Field('lastViewedDate')
    obj_id = Field('objID')
    obj_obj_code = Field('objObjCode')
    op_task_id = Field('opTaskID')
    priority = Field('priority')
    project_id = Field('projectID')
    reference_object_commit_date = Field('referenceObjectCommitDate')
    reference_object_name = Field('referenceObjectName')
    security_root_id = Field('securityRootID')
    security_root_obj_code = Field('securityRootObjCode')
    snooze_date = Field('snoozeDate')
    task_id = Field('taskID')
    user_id = Field('userID')
    assignment = Reference('assignment')
    customer = Reference('customer')
    op_task = Reference('opTask')
    project = Reference('project')
    task = Reference('task')
    user = Reference('user')

    def make_top_priority(self, obj_code=None, assignable_id=None, user_id=None):
        """
        The ``makeTopPriority`` action.
        
        :param obj_code: objCode (type: ``string``)
        :param assignable_id: assignableID (type: ``string``)
        :param user_id: userID (type: ``string``)
        """
        params = {}
        if obj_code is not None: params['objCode'] = obj_code
        if assignable_id  is not None: params['assignableID '] = assignable_id 
        if user_id is not None: params['userID'] = user_id
        data = self.session.put(self.api_url()+'/makeTopPriority', params)
        

    def mark_viewed(self):
        """
        The ``markViewed`` action.
        
        """
        params = {}
        
        data = self.session.put(self.api_url()+'/markViewed', params)
        

api.register(WorkItem)
