"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.13
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eZmaxApi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from eZmaxApi.exceptions import ApiAttributeError


def lazy_import():
    from eZmaxApi.model.ezsignfoldertype_request_compound_all_of import EzsignfoldertypeRequestCompoundAllOf
    from eZmaxApi.model.ezsignfoldertype_response import EzsignfoldertypeResponse
    from eZmaxApi.model.field_e_ezsignfoldertype_disposal import FieldEEzsignfoldertypeDisposal
    from eZmaxApi.model.field_e_ezsignfoldertype_privacylevel import FieldEEzsignfoldertypePrivacylevel
    from eZmaxApi.model.field_e_ezsignfoldertype_sendreminderfrequency import FieldEEzsignfoldertypeSendreminderfrequency
    from eZmaxApi.model.field_i_ezsignfoldertype_archivaldays import FieldIEzsignfoldertypeArchivaldays
    from eZmaxApi.model.field_i_ezsignfoldertype_deadlinedays import FieldIEzsignfoldertypeDeadlinedays
    from eZmaxApi.model.field_i_ezsignfoldertype_disposaldays import FieldIEzsignfoldertypeDisposaldays
    from eZmaxApi.model.field_pki_billingentityinternal_id import FieldPkiBillingentityinternalID
    from eZmaxApi.model.field_pki_branding_id import FieldPkiBrandingID
    from eZmaxApi.model.field_pki_ezsignfoldertype_id import FieldPkiEzsignfoldertypeID
    from eZmaxApi.model.field_pki_ezsigntsarequirement_id import FieldPkiEzsigntsarequirementID
    from eZmaxApi.model.field_pki_user_id import FieldPkiUserID
    from eZmaxApi.model.field_pki_usergroup_id import FieldPkiUsergroupID
    from eZmaxApi.model.multilingual_ezsignfoldertype_name import MultilingualEzsignfoldertypeName
    globals()['EzsignfoldertypeRequestCompoundAllOf'] = EzsignfoldertypeRequestCompoundAllOf
    globals()['EzsignfoldertypeResponse'] = EzsignfoldertypeResponse
    globals()['FieldEEzsignfoldertypeDisposal'] = FieldEEzsignfoldertypeDisposal
    globals()['FieldEEzsignfoldertypePrivacylevel'] = FieldEEzsignfoldertypePrivacylevel
    globals()['FieldEEzsignfoldertypeSendreminderfrequency'] = FieldEEzsignfoldertypeSendreminderfrequency
    globals()['FieldIEzsignfoldertypeArchivaldays'] = FieldIEzsignfoldertypeArchivaldays
    globals()['FieldIEzsignfoldertypeDeadlinedays'] = FieldIEzsignfoldertypeDeadlinedays
    globals()['FieldIEzsignfoldertypeDisposaldays'] = FieldIEzsignfoldertypeDisposaldays
    globals()['FieldPkiBillingentityinternalID'] = FieldPkiBillingentityinternalID
    globals()['FieldPkiBrandingID'] = FieldPkiBrandingID
    globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
    globals()['FieldPkiEzsigntsarequirementID'] = FieldPkiEzsigntsarequirementID
    globals()['FieldPkiUserID'] = FieldPkiUserID
    globals()['FieldPkiUsergroupID'] = FieldPkiUsergroupID
    globals()['MultilingualEzsignfoldertypeName'] = MultilingualEzsignfoldertypeName


class EzsignfoldertypeResponseCompound(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'pki_ezsignfoldertype_id': (FieldPkiEzsignfoldertypeID,),  # noqa: E501
            'obj_ezsignfoldertype_name': (MultilingualEzsignfoldertypeName,),  # noqa: E501
            'fki_branding_id': (FieldPkiBrandingID,),  # noqa: E501
            's_branding_description_x': (str,),  # noqa: E501
            'e_ezsignfoldertype_privacylevel': (FieldEEzsignfoldertypePrivacylevel,),  # noqa: E501
            'i_ezsignfoldertype_archivaldays': (FieldIEzsignfoldertypeArchivaldays,),  # noqa: E501
            'e_ezsignfoldertype_disposal': (FieldEEzsignfoldertypeDisposal,),  # noqa: E501
            'i_ezsignfoldertype_deadlinedays': (FieldIEzsignfoldertypeDeadlinedays,),  # noqa: E501
            'b_ezsignfoldertype_sendattatchmentsigner': (bool,),  # noqa: E501
            'b_ezsignfoldertype_sendsignedtodocumentowner': (bool,),  # noqa: E501
            'b_ezsignfoldertype_sendsignedtofolderowner': (bool,),  # noqa: E501
            'b_ezsignfoldertype_sendsignedtocolleague': (bool,),  # noqa: E501
            'b_ezsignfoldertype_sendsummarytodocumentowner': (bool,),  # noqa: E501
            'b_ezsignfoldertype_sendsummarytofolderowner': (bool,),  # noqa: E501
            'b_ezsignfoldertype_sendsummarytocolleague': (bool,),  # noqa: E501
            'b_ezsignfoldertype_includeproofsigner': (bool,),  # noqa: E501
            'b_ezsignfoldertype_includeproofuser': (bool,),  # noqa: E501
            'b_ezsignfoldertype_isactive': (bool,),  # noqa: E501
            'fki_billingentityinternal_id': (FieldPkiBillingentityinternalID,),  # noqa: E501
            'fki_usergroup_id': (FieldPkiUsergroupID,),  # noqa: E501
            'fki_usergroup_id_restricted': (FieldPkiUsergroupID,),  # noqa: E501
            'fki_ezsigntsarequirement_id': (FieldPkiEzsigntsarequirementID,),  # noqa: E501
            's_billingentityinternal_description_x': (str,),  # noqa: E501
            's_ezsigntsarequirement_description_x': (str,),  # noqa: E501
            's_email_address_signed': (str,),  # noqa: E501
            's_email_address_summary': (str,),  # noqa: E501
            's_usergroup_name_x': (str,),  # noqa: E501
            's_usergroup_name_x_restricted': (str,),  # noqa: E501
            'e_ezsignfoldertype_sendreminderfrequency': (FieldEEzsignfoldertypeSendreminderfrequency,),  # noqa: E501
            'i_ezsignfoldertype_disposaldays': (FieldIEzsignfoldertypeDisposaldays,),  # noqa: E501
            'b_ezsignfoldertype_sendsignedtofullgroup': (bool,),  # noqa: E501
            'b_ezsignfoldertype_sendsignedtolimitedgroup': (bool,),  # noqa: E501
            'b_ezsignfoldertype_sendsummarytofullgroup': (bool,),  # noqa: E501
            'b_ezsignfoldertype_sendsummarytolimitedgroup': (bool,),  # noqa: E501
            'a_fki_user_id_signed': ([FieldPkiUserID],),  # noqa: E501
            'a_fki_user_id_summary': ([FieldPkiUserID],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pki_ezsignfoldertype_id': 'pkiEzsignfoldertypeID',  # noqa: E501
        'obj_ezsignfoldertype_name': 'objEzsignfoldertypeName',  # noqa: E501
        'fki_branding_id': 'fkiBrandingID',  # noqa: E501
        's_branding_description_x': 'sBrandingDescriptionX',  # noqa: E501
        'e_ezsignfoldertype_privacylevel': 'eEzsignfoldertypePrivacylevel',  # noqa: E501
        'i_ezsignfoldertype_archivaldays': 'iEzsignfoldertypeArchivaldays',  # noqa: E501
        'e_ezsignfoldertype_disposal': 'eEzsignfoldertypeDisposal',  # noqa: E501
        'i_ezsignfoldertype_deadlinedays': 'iEzsignfoldertypeDeadlinedays',  # noqa: E501
        'b_ezsignfoldertype_sendattatchmentsigner': 'bEzsignfoldertypeSendattatchmentsigner',  # noqa: E501
        'b_ezsignfoldertype_sendsignedtodocumentowner': 'bEzsignfoldertypeSendsignedtodocumentowner',  # noqa: E501
        'b_ezsignfoldertype_sendsignedtofolderowner': 'bEzsignfoldertypeSendsignedtofolderowner',  # noqa: E501
        'b_ezsignfoldertype_sendsignedtocolleague': 'bEzsignfoldertypeSendsignedtocolleague',  # noqa: E501
        'b_ezsignfoldertype_sendsummarytodocumentowner': 'bEzsignfoldertypeSendsummarytodocumentowner',  # noqa: E501
        'b_ezsignfoldertype_sendsummarytofolderowner': 'bEzsignfoldertypeSendsummarytofolderowner',  # noqa: E501
        'b_ezsignfoldertype_sendsummarytocolleague': 'bEzsignfoldertypeSendsummarytocolleague',  # noqa: E501
        'b_ezsignfoldertype_includeproofsigner': 'bEzsignfoldertypeIncludeproofsigner',  # noqa: E501
        'b_ezsignfoldertype_includeproofuser': 'bEzsignfoldertypeIncludeproofuser',  # noqa: E501
        'b_ezsignfoldertype_isactive': 'bEzsignfoldertypeIsactive',  # noqa: E501
        'fki_billingentityinternal_id': 'fkiBillingentityinternalID',  # noqa: E501
        'fki_usergroup_id': 'fkiUsergroupID',  # noqa: E501
        'fki_usergroup_id_restricted': 'fkiUsergroupIDRestricted',  # noqa: E501
        'fki_ezsigntsarequirement_id': 'fkiEzsigntsarequirementID',  # noqa: E501
        's_billingentityinternal_description_x': 'sBillingentityinternalDescriptionX',  # noqa: E501
        's_ezsigntsarequirement_description_x': 'sEzsigntsarequirementDescriptionX',  # noqa: E501
        's_email_address_signed': 'sEmailAddressSigned',  # noqa: E501
        's_email_address_summary': 'sEmailAddressSummary',  # noqa: E501
        's_usergroup_name_x': 'sUsergroupNameX',  # noqa: E501
        's_usergroup_name_x_restricted': 'sUsergroupNameXRestricted',  # noqa: E501
        'e_ezsignfoldertype_sendreminderfrequency': 'eEzsignfoldertypeSendreminderfrequency',  # noqa: E501
        'i_ezsignfoldertype_disposaldays': 'iEzsignfoldertypeDisposaldays',  # noqa: E501
        'b_ezsignfoldertype_sendsignedtofullgroup': 'bEzsignfoldertypeSendsignedtofullgroup',  # noqa: E501
        'b_ezsignfoldertype_sendsignedtolimitedgroup': 'bEzsignfoldertypeSendsignedtolimitedgroup',  # noqa: E501
        'b_ezsignfoldertype_sendsummarytofullgroup': 'bEzsignfoldertypeSendsummarytofullgroup',  # noqa: E501
        'b_ezsignfoldertype_sendsummarytolimitedgroup': 'bEzsignfoldertypeSendsummarytolimitedgroup',  # noqa: E501
        'a_fki_user_id_signed': 'a_fkiUserIDSigned',  # noqa: E501
        'a_fki_user_id_summary': 'a_fkiUserIDSummary',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EzsignfoldertypeResponseCompound - a model defined in OpenAPI

        Keyword Args:
            pki_ezsignfoldertype_id (FieldPkiEzsignfoldertypeID):
            obj_ezsignfoldertype_name (MultilingualEzsignfoldertypeName):
            fki_branding_id (FieldPkiBrandingID):
            s_branding_description_x (str): The Description of the Branding in the language of the requester
            e_ezsignfoldertype_privacylevel (FieldEEzsignfoldertypePrivacylevel):
            i_ezsignfoldertype_archivaldays (FieldIEzsignfoldertypeArchivaldays):
            e_ezsignfoldertype_disposal (FieldEEzsignfoldertypeDisposal):
            i_ezsignfoldertype_deadlinedays (FieldIEzsignfoldertypeDeadlinedays):
            b_ezsignfoldertype_sendattatchmentsigner (bool): Whether we send the Ezsigndocument and the proof as attachment in the email
            b_ezsignfoldertype_sendsignedtodocumentowner (bool): Whether we send the signed Ezsigndocument to the Ezsigndocument's owner
            b_ezsignfoldertype_sendsignedtofolderowner (bool): Whether we send the signed Ezsigndocument to the Ezsignfolder's owner
            b_ezsignfoldertype_sendsignedtocolleague (bool): Whether we send the signed Ezsigndocument to the colleagues
            b_ezsignfoldertype_sendsummarytodocumentowner (bool): Whether we send the summary to the Ezsigndocument's owner
            b_ezsignfoldertype_sendsummarytofolderowner (bool): Whether we send the summary to the Ezsignfolder's owner
            b_ezsignfoldertype_sendsummarytocolleague (bool): Whether we send the summary to the colleagues
            b_ezsignfoldertype_includeproofsigner (bool): Whether we include the proof with the signed Ezsigndocument for Ezsignsigners
            b_ezsignfoldertype_includeproofuser (bool): Whether we include the proof with the signed Ezsigndocument for users
            b_ezsignfoldertype_isactive (bool): Whether the Ezsignfoldertype is active or not
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            fki_billingentityinternal_id (FieldPkiBillingentityinternalID): [optional]  # noqa: E501
            fki_usergroup_id (FieldPkiUsergroupID): [optional]  # noqa: E501
            fki_usergroup_id_restricted (FieldPkiUsergroupID): [optional]  # noqa: E501
            fki_ezsigntsarequirement_id (FieldPkiEzsigntsarequirementID): [optional]  # noqa: E501
            s_billingentityinternal_description_x (str): The description of the Billingentityinternal in the language of the requester. [optional]  # noqa: E501
            s_ezsigntsarequirement_description_x (str): The description of the Ezsigntsarequirement in the language of the requester. [optional]  # noqa: E501
            s_email_address_signed (str): The email address.. [optional]  # noqa: E501
            s_email_address_summary (str): The email address.. [optional]  # noqa: E501
            s_usergroup_name_x (str): The Name of the Usergroup in the language of the requester. [optional]  # noqa: E501
            s_usergroup_name_x_restricted (str): The Name of the Usergroup in the language of the requester. [optional]  # noqa: E501
            e_ezsignfoldertype_sendreminderfrequency (FieldEEzsignfoldertypeSendreminderfrequency): [optional]  # noqa: E501
            i_ezsignfoldertype_disposaldays (FieldIEzsignfoldertypeDisposaldays): [optional]  # noqa: E501
            b_ezsignfoldertype_sendsignedtofullgroup (bool): Whether we send the signed Ezsigndocument to the Usergroup that has acces to all Ezsignfolders. [optional]  # noqa: E501
            b_ezsignfoldertype_sendsignedtolimitedgroup (bool): Whether we send the signed Ezsigndocument to the Usergroup that has acces to only their own Ezsignfolders. [optional]  # noqa: E501
            b_ezsignfoldertype_sendsummarytofullgroup (bool): Whether we send the summary to the Usergroup that has acces to all Ezsignfolders. [optional]  # noqa: E501
            b_ezsignfoldertype_sendsummarytolimitedgroup (bool): Whether we send the summary to the Usergroup that has acces to only their own Ezsignfolders. [optional]  # noqa: E501
            a_fki_user_id_signed ([FieldPkiUserID]): [optional]  # noqa: E501
            a_fki_user_id_summary ([FieldPkiUserID]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """EzsignfoldertypeResponseCompound - a model defined in OpenAPI

        Keyword Args:
            pki_ezsignfoldertype_id (FieldPkiEzsignfoldertypeID):
            obj_ezsignfoldertype_name (MultilingualEzsignfoldertypeName):
            fki_branding_id (FieldPkiBrandingID):
            s_branding_description_x (str): The Description of the Branding in the language of the requester
            e_ezsignfoldertype_privacylevel (FieldEEzsignfoldertypePrivacylevel):
            i_ezsignfoldertype_archivaldays (FieldIEzsignfoldertypeArchivaldays):
            e_ezsignfoldertype_disposal (FieldEEzsignfoldertypeDisposal):
            i_ezsignfoldertype_deadlinedays (FieldIEzsignfoldertypeDeadlinedays):
            b_ezsignfoldertype_sendattatchmentsigner (bool): Whether we send the Ezsigndocument and the proof as attachment in the email
            b_ezsignfoldertype_sendsignedtodocumentowner (bool): Whether we send the signed Ezsigndocument to the Ezsigndocument's owner
            b_ezsignfoldertype_sendsignedtofolderowner (bool): Whether we send the signed Ezsigndocument to the Ezsignfolder's owner
            b_ezsignfoldertype_sendsignedtocolleague (bool): Whether we send the signed Ezsigndocument to the colleagues
            b_ezsignfoldertype_sendsummarytodocumentowner (bool): Whether we send the summary to the Ezsigndocument's owner
            b_ezsignfoldertype_sendsummarytofolderowner (bool): Whether we send the summary to the Ezsignfolder's owner
            b_ezsignfoldertype_sendsummarytocolleague (bool): Whether we send the summary to the colleagues
            b_ezsignfoldertype_includeproofsigner (bool): Whether we include the proof with the signed Ezsigndocument for Ezsignsigners
            b_ezsignfoldertype_includeproofuser (bool): Whether we include the proof with the signed Ezsigndocument for users
            b_ezsignfoldertype_isactive (bool): Whether the Ezsignfoldertype is active or not
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            fki_billingentityinternal_id (FieldPkiBillingentityinternalID): [optional]  # noqa: E501
            fki_usergroup_id (FieldPkiUsergroupID): [optional]  # noqa: E501
            fki_usergroup_id_restricted (FieldPkiUsergroupID): [optional]  # noqa: E501
            fki_ezsigntsarequirement_id (FieldPkiEzsigntsarequirementID): [optional]  # noqa: E501
            s_billingentityinternal_description_x (str): The description of the Billingentityinternal in the language of the requester. [optional]  # noqa: E501
            s_ezsigntsarequirement_description_x (str): The description of the Ezsigntsarequirement in the language of the requester. [optional]  # noqa: E501
            s_email_address_signed (str): The email address.. [optional]  # noqa: E501
            s_email_address_summary (str): The email address.. [optional]  # noqa: E501
            s_usergroup_name_x (str): The Name of the Usergroup in the language of the requester. [optional]  # noqa: E501
            s_usergroup_name_x_restricted (str): The Name of the Usergroup in the language of the requester. [optional]  # noqa: E501
            e_ezsignfoldertype_sendreminderfrequency (FieldEEzsignfoldertypeSendreminderfrequency): [optional]  # noqa: E501
            i_ezsignfoldertype_disposaldays (FieldIEzsignfoldertypeDisposaldays): [optional]  # noqa: E501
            b_ezsignfoldertype_sendsignedtofullgroup (bool): Whether we send the signed Ezsigndocument to the Usergroup that has acces to all Ezsignfolders. [optional]  # noqa: E501
            b_ezsignfoldertype_sendsignedtolimitedgroup (bool): Whether we send the signed Ezsigndocument to the Usergroup that has acces to only their own Ezsignfolders. [optional]  # noqa: E501
            b_ezsignfoldertype_sendsummarytofullgroup (bool): Whether we send the summary to the Usergroup that has acces to all Ezsignfolders. [optional]  # noqa: E501
            b_ezsignfoldertype_sendsummarytolimitedgroup (bool): Whether we send the summary to the Usergroup that has acces to only their own Ezsignfolders. [optional]  # noqa: E501
            a_fki_user_id_signed ([FieldPkiUserID]): [optional]  # noqa: E501
            a_fki_user_id_summary ([FieldPkiUserID]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              EzsignfoldertypeRequestCompoundAllOf,
              EzsignfoldertypeResponse,
          ],
          'oneOf': [
          ],
        }
