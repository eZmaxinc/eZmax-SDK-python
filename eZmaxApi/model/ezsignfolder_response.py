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
    from eZmaxApi.model.common_audit import CommonAudit
    from eZmaxApi.model.field_e_ezsignfolder_sendreminderfrequency import FieldEEzsignfolderSendreminderfrequency
    from eZmaxApi.model.field_e_ezsignfolder_step import FieldEEzsignfolderStep
    from eZmaxApi.model.field_pki_billingentityinternal_id import FieldPkiBillingentityinternalID
    from eZmaxApi.model.field_pki_ezsignfolder_id import FieldPkiEzsignfolderID
    from eZmaxApi.model.field_pki_ezsignfoldertype_id import FieldPkiEzsignfoldertypeID
    from eZmaxApi.model.field_pki_ezsigntsarequirement_id import FieldPkiEzsigntsarequirementID
    globals()['CommonAudit'] = CommonAudit
    globals()['FieldEEzsignfolderSendreminderfrequency'] = FieldEEzsignfolderSendreminderfrequency
    globals()['FieldEEzsignfolderStep'] = FieldEEzsignfolderStep
    globals()['FieldPkiBillingentityinternalID'] = FieldPkiBillingentityinternalID
    globals()['FieldPkiEzsignfolderID'] = FieldPkiEzsignfolderID
    globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
    globals()['FieldPkiEzsigntsarequirementID'] = FieldPkiEzsigntsarequirementID


class EzsignfolderResponse(ModelNormal):
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
            'pki_ezsignfolder_id': (FieldPkiEzsignfolderID,),  # noqa: E501
            'fki_ezsignfoldertype_id': (FieldPkiEzsignfoldertypeID,),  # noqa: E501
            's_ezsignfoldertype_name_x': (str,),  # noqa: E501
            'fki_billingentityinternal_id': (FieldPkiBillingentityinternalID,),  # noqa: E501
            's_billingentityinternal_description_x': (str,),  # noqa: E501
            'fki_ezsigntsarequirement_id': (FieldPkiEzsigntsarequirementID,),  # noqa: E501
            's_ezsigntsarequirement_description_x': (str,),  # noqa: E501
            's_ezsignfolder_description': (str,),  # noqa: E501
            't_ezsignfolder_note': (str,),  # noqa: E501
            'b_ezsignfolder_isdisposable': (bool,),  # noqa: E501
            'e_ezsignfolder_sendreminderfrequency': (FieldEEzsignfolderSendreminderfrequency,),  # noqa: E501
            'e_ezsignfolder_step': (FieldEEzsignfolderStep,),  # noqa: E501
            't_ezsignfolder_message': (str,),  # noqa: E501
            'obj_audit': (CommonAudit,),  # noqa: E501
            'dt_ezsignfolder_duedate': (str,),  # noqa: E501
            'dt_ezsignfolder_sentdate': (str,),  # noqa: E501
            'dt_ezsignfolder_scheduledarchive': (str,),  # noqa: E501
            'dt_ezsignfolder_scheduleddispose': (str,),  # noqa: E501
            'dt_ezsignfolder_close': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pki_ezsignfolder_id': 'pkiEzsignfolderID',  # noqa: E501
        'fki_ezsignfoldertype_id': 'fkiEzsignfoldertypeID',  # noqa: E501
        's_ezsignfoldertype_name_x': 'sEzsignfoldertypeNameX',  # noqa: E501
        'fki_billingentityinternal_id': 'fkiBillingentityinternalID',  # noqa: E501
        's_billingentityinternal_description_x': 'sBillingentityinternalDescriptionX',  # noqa: E501
        'fki_ezsigntsarequirement_id': 'fkiEzsigntsarequirementID',  # noqa: E501
        's_ezsigntsarequirement_description_x': 'sEzsigntsarequirementDescriptionX',  # noqa: E501
        's_ezsignfolder_description': 'sEzsignfolderDescription',  # noqa: E501
        't_ezsignfolder_note': 'tEzsignfolderNote',  # noqa: E501
        'b_ezsignfolder_isdisposable': 'bEzsignfolderIsdisposable',  # noqa: E501
        'e_ezsignfolder_sendreminderfrequency': 'eEzsignfolderSendreminderfrequency',  # noqa: E501
        'e_ezsignfolder_step': 'eEzsignfolderStep',  # noqa: E501
        't_ezsignfolder_message': 'tEzsignfolderMessage',  # noqa: E501
        'obj_audit': 'objAudit',  # noqa: E501
        'dt_ezsignfolder_duedate': 'dtEzsignfolderDuedate',  # noqa: E501
        'dt_ezsignfolder_sentdate': 'dtEzsignfolderSentdate',  # noqa: E501
        'dt_ezsignfolder_scheduledarchive': 'dtEzsignfolderScheduledarchive',  # noqa: E501
        'dt_ezsignfolder_scheduleddispose': 'dtEzsignfolderScheduleddispose',  # noqa: E501
        'dt_ezsignfolder_close': 'dtEzsignfolderClose',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, pki_ezsignfolder_id, fki_ezsignfoldertype_id, s_ezsignfoldertype_name_x, fki_billingentityinternal_id, s_billingentityinternal_description_x, fki_ezsigntsarequirement_id, s_ezsigntsarequirement_description_x, s_ezsignfolder_description, t_ezsignfolder_note, b_ezsignfolder_isdisposable, e_ezsignfolder_sendreminderfrequency, e_ezsignfolder_step, t_ezsignfolder_message, obj_audit, *args, **kwargs):  # noqa: E501
        """EzsignfolderResponse - a model defined in OpenAPI

        Args:
            pki_ezsignfolder_id (FieldPkiEzsignfolderID):
            fki_ezsignfoldertype_id (FieldPkiEzsignfoldertypeID):
            s_ezsignfoldertype_name_x (str): The name of the Ezsignfoldertype in the language of the requester
            fki_billingentityinternal_id (FieldPkiBillingentityinternalID):
            s_billingentityinternal_description_x (str): The description of the Billingentityinternal in the language of the requester
            fki_ezsigntsarequirement_id (FieldPkiEzsigntsarequirementID):
            s_ezsigntsarequirement_description_x (str): The description of the Ezsigntsarequirement in the language of the requester
            s_ezsignfolder_description (str): The description of the Ezsignfolder
            t_ezsignfolder_note (str): Note about the Ezsignfolder
            b_ezsignfolder_isdisposable (bool): If the Ezsigndocument can be disposed
            e_ezsignfolder_sendreminderfrequency (FieldEEzsignfolderSendreminderfrequency):
            e_ezsignfolder_step (FieldEEzsignfolderStep):
            t_ezsignfolder_message (str): A custom text message that will be added to the email sent.
            obj_audit (CommonAudit):

        Keyword Args:
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
            dt_ezsignfolder_duedate (str): The maximum date and time at which the Ezsignfolder can be signed.. [optional]  # noqa: E501
            dt_ezsignfolder_sentdate (str): The date and time at which the Ezsign folder was sent the last time.. [optional]  # noqa: E501
            dt_ezsignfolder_scheduledarchive (str): The scheduled date and time at which the Ezsignfolder should be archived.. [optional]  # noqa: E501
            dt_ezsignfolder_scheduleddispose (str): The scheduled date at which the Ezsignfolder should be Disposed.. [optional]  # noqa: E501
            dt_ezsignfolder_close (str): The date and time at which the folder was closed. Either by applying the last signature or by completing it prematurely.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
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

        self.pki_ezsignfolder_id = pki_ezsignfolder_id
        self.fki_ezsignfoldertype_id = fki_ezsignfoldertype_id
        self.s_ezsignfoldertype_name_x = s_ezsignfoldertype_name_x
        self.fki_billingentityinternal_id = fki_billingentityinternal_id
        self.s_billingentityinternal_description_x = s_billingentityinternal_description_x
        self.fki_ezsigntsarequirement_id = fki_ezsigntsarequirement_id
        self.s_ezsigntsarequirement_description_x = s_ezsigntsarequirement_description_x
        self.s_ezsignfolder_description = s_ezsignfolder_description
        self.t_ezsignfolder_note = t_ezsignfolder_note
        self.b_ezsignfolder_isdisposable = b_ezsignfolder_isdisposable
        self.e_ezsignfolder_sendreminderfrequency = e_ezsignfolder_sendreminderfrequency
        self.e_ezsignfolder_step = e_ezsignfolder_step
        self.t_ezsignfolder_message = t_ezsignfolder_message
        self.obj_audit = obj_audit
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
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
    ])

    @convert_js_args_to_python_args
    def __init__(self, pki_ezsignfolder_id, fki_ezsignfoldertype_id, s_ezsignfoldertype_name_x, fki_billingentityinternal_id, s_billingentityinternal_description_x, fki_ezsigntsarequirement_id, s_ezsigntsarequirement_description_x, s_ezsignfolder_description, t_ezsignfolder_note, b_ezsignfolder_isdisposable, e_ezsignfolder_sendreminderfrequency, e_ezsignfolder_step, t_ezsignfolder_message, obj_audit, *args, **kwargs):  # noqa: E501
        """EzsignfolderResponse - a model defined in OpenAPI

        Args:
            pki_ezsignfolder_id (FieldPkiEzsignfolderID):
            fki_ezsignfoldertype_id (FieldPkiEzsignfoldertypeID):
            s_ezsignfoldertype_name_x (str): The name of the Ezsignfoldertype in the language of the requester
            fki_billingentityinternal_id (FieldPkiBillingentityinternalID):
            s_billingentityinternal_description_x (str): The description of the Billingentityinternal in the language of the requester
            fki_ezsigntsarequirement_id (FieldPkiEzsigntsarequirementID):
            s_ezsigntsarequirement_description_x (str): The description of the Ezsigntsarequirement in the language of the requester
            s_ezsignfolder_description (str): The description of the Ezsignfolder
            t_ezsignfolder_note (str): Note about the Ezsignfolder
            b_ezsignfolder_isdisposable (bool): If the Ezsigndocument can be disposed
            e_ezsignfolder_sendreminderfrequency (FieldEEzsignfolderSendreminderfrequency):
            e_ezsignfolder_step (FieldEEzsignfolderStep):
            t_ezsignfolder_message (str): A custom text message that will be added to the email sent.
            obj_audit (CommonAudit):

        Keyword Args:
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
            dt_ezsignfolder_duedate (str): The maximum date and time at which the Ezsignfolder can be signed.. [optional]  # noqa: E501
            dt_ezsignfolder_sentdate (str): The date and time at which the Ezsign folder was sent the last time.. [optional]  # noqa: E501
            dt_ezsignfolder_scheduledarchive (str): The scheduled date and time at which the Ezsignfolder should be archived.. [optional]  # noqa: E501
            dt_ezsignfolder_scheduleddispose (str): The scheduled date at which the Ezsignfolder should be Disposed.. [optional]  # noqa: E501
            dt_ezsignfolder_close (str): The date and time at which the folder was closed. Either by applying the last signature or by completing it prematurely.. [optional]  # noqa: E501
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

        self.pki_ezsignfolder_id = pki_ezsignfolder_id
        self.fki_ezsignfoldertype_id = fki_ezsignfoldertype_id
        self.s_ezsignfoldertype_name_x = s_ezsignfoldertype_name_x
        self.fki_billingentityinternal_id = fki_billingentityinternal_id
        self.s_billingentityinternal_description_x = s_billingentityinternal_description_x
        self.fki_ezsigntsarequirement_id = fki_ezsigntsarequirement_id
        self.s_ezsigntsarequirement_description_x = s_ezsigntsarequirement_description_x
        self.s_ezsignfolder_description = s_ezsignfolder_description
        self.t_ezsignfolder_note = t_ezsignfolder_note
        self.b_ezsignfolder_isdisposable = b_ezsignfolder_isdisposable
        self.e_ezsignfolder_sendreminderfrequency = e_ezsignfolder_sendreminderfrequency
        self.e_ezsignfolder_step = e_ezsignfolder_step
        self.t_ezsignfolder_message = t_ezsignfolder_message
        self.obj_audit = obj_audit
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
