"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.16
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
    from eZmaxApi.model.custom_dropdown_element_request_compound import CustomDropdownElementRequestCompound
    from eZmaxApi.model.ezsignformfield_request_compound import EzsignformfieldRequestCompound
    from eZmaxApi.model.ezsignformfieldgroup_request import EzsignformfieldgroupRequest
    from eZmaxApi.model.ezsignformfieldgroup_request_compound_all_of import EzsignformfieldgroupRequestCompoundAllOf
    from eZmaxApi.model.ezsignformfieldgroupsigner_request_compound import EzsignformfieldgroupsignerRequestCompound
    from eZmaxApi.model.field_e_ezsignformfieldgroup_signerrequirement import FieldEEzsignformfieldgroupSignerrequirement
    from eZmaxApi.model.field_e_ezsignformfieldgroup_tooltipposition import FieldEEzsignformfieldgroupTooltipposition
    from eZmaxApi.model.field_e_ezsignformfieldgroup_type import FieldEEzsignformfieldgroupType
    from eZmaxApi.model.field_i_ezsignformfieldgroup_filledmax import FieldIEzsignformfieldgroupFilledmax
    from eZmaxApi.model.field_i_ezsignformfieldgroup_filledmin import FieldIEzsignformfieldgroupFilledmin
    from eZmaxApi.model.field_i_ezsignformfieldgroup_maxlength import FieldIEzsignformfieldgroupMaxlength
    from eZmaxApi.model.field_i_ezsignformfieldgroup_step import FieldIEzsignformfieldgroupStep
    from eZmaxApi.model.field_pki_ezsigndocument_id import FieldPkiEzsigndocumentID
    from eZmaxApi.model.field_pki_ezsignformfieldgroup_id import FieldPkiEzsignformfieldgroupID
    globals()['CustomDropdownElementRequestCompound'] = CustomDropdownElementRequestCompound
    globals()['EzsignformfieldRequestCompound'] = EzsignformfieldRequestCompound
    globals()['EzsignformfieldgroupRequest'] = EzsignformfieldgroupRequest
    globals()['EzsignformfieldgroupRequestCompoundAllOf'] = EzsignformfieldgroupRequestCompoundAllOf
    globals()['EzsignformfieldgroupsignerRequestCompound'] = EzsignformfieldgroupsignerRequestCompound
    globals()['FieldEEzsignformfieldgroupSignerrequirement'] = FieldEEzsignformfieldgroupSignerrequirement
    globals()['FieldEEzsignformfieldgroupTooltipposition'] = FieldEEzsignformfieldgroupTooltipposition
    globals()['FieldEEzsignformfieldgroupType'] = FieldEEzsignformfieldgroupType
    globals()['FieldIEzsignformfieldgroupFilledmax'] = FieldIEzsignformfieldgroupFilledmax
    globals()['FieldIEzsignformfieldgroupFilledmin'] = FieldIEzsignformfieldgroupFilledmin
    globals()['FieldIEzsignformfieldgroupMaxlength'] = FieldIEzsignformfieldgroupMaxlength
    globals()['FieldIEzsignformfieldgroupStep'] = FieldIEzsignformfieldgroupStep
    globals()['FieldPkiEzsigndocumentID'] = FieldPkiEzsigndocumentID
    globals()['FieldPkiEzsignformfieldgroupID'] = FieldPkiEzsignformfieldgroupID


class EzsignformfieldgroupRequestCompound(ModelComposed):
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
            'fki_ezsigndocument_id': (FieldPkiEzsigndocumentID,),  # noqa: E501
            'e_ezsignformfieldgroup_type': (FieldEEzsignformfieldgroupType,),  # noqa: E501
            'e_ezsignformfieldgroup_signerrequirement': (FieldEEzsignformfieldgroupSignerrequirement,),  # noqa: E501
            's_ezsignformfieldgroup_label': (str,),  # noqa: E501
            'i_ezsignformfieldgroup_step': (FieldIEzsignformfieldgroupStep,),  # noqa: E501
            's_ezsignformfieldgroup_defaultvalue': (str,),  # noqa: E501
            'i_ezsignformfieldgroup_filledmin': (FieldIEzsignformfieldgroupFilledmin,),  # noqa: E501
            'i_ezsignformfieldgroup_filledmax': (FieldIEzsignformfieldgroupFilledmax,),  # noqa: E501
            'b_ezsignformfieldgroup_readonly': (bool,),  # noqa: E501
            'a_obj_ezsignformfieldgroupsigner': ([EzsignformfieldgroupsignerRequestCompound],),  # noqa: E501
            'a_obj_ezsignformfield': ([EzsignformfieldRequestCompound],),  # noqa: E501
            'pki_ezsignformfieldgroup_id': (FieldPkiEzsignformfieldgroupID,),  # noqa: E501
            'i_ezsignformfieldgroup_maxlength': (FieldIEzsignformfieldgroupMaxlength,),  # noqa: E501
            'b_ezsignformfieldgroup_encrypted': (bool,),  # noqa: E501
            's_ezsignformfieldgroup_regexp': (str,),  # noqa: E501
            't_ezsignformfieldgroup_tooltip': (str,),  # noqa: E501
            'e_ezsignformfieldgroup_tooltipposition': (FieldEEzsignformfieldgroupTooltipposition,),  # noqa: E501
            'a_obj_dropdown_element': ([CustomDropdownElementRequestCompound],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fki_ezsigndocument_id': 'fkiEzsigndocumentID',  # noqa: E501
        'e_ezsignformfieldgroup_type': 'eEzsignformfieldgroupType',  # noqa: E501
        'e_ezsignformfieldgroup_signerrequirement': 'eEzsignformfieldgroupSignerrequirement',  # noqa: E501
        's_ezsignformfieldgroup_label': 'sEzsignformfieldgroupLabel',  # noqa: E501
        'i_ezsignformfieldgroup_step': 'iEzsignformfieldgroupStep',  # noqa: E501
        's_ezsignformfieldgroup_defaultvalue': 'sEzsignformfieldgroupDefaultvalue',  # noqa: E501
        'i_ezsignformfieldgroup_filledmin': 'iEzsignformfieldgroupFilledmin',  # noqa: E501
        'i_ezsignformfieldgroup_filledmax': 'iEzsignformfieldgroupFilledmax',  # noqa: E501
        'b_ezsignformfieldgroup_readonly': 'bEzsignformfieldgroupReadonly',  # noqa: E501
        'a_obj_ezsignformfieldgroupsigner': 'a_objEzsignformfieldgroupsigner',  # noqa: E501
        'a_obj_ezsignformfield': 'a_objEzsignformfield',  # noqa: E501
        'pki_ezsignformfieldgroup_id': 'pkiEzsignformfieldgroupID',  # noqa: E501
        'i_ezsignformfieldgroup_maxlength': 'iEzsignformfieldgroupMaxlength',  # noqa: E501
        'b_ezsignformfieldgroup_encrypted': 'bEzsignformfieldgroupEncrypted',  # noqa: E501
        's_ezsignformfieldgroup_regexp': 'sEzsignformfieldgroupRegexp',  # noqa: E501
        't_ezsignformfieldgroup_tooltip': 'tEzsignformfieldgroupTooltip',  # noqa: E501
        'e_ezsignformfieldgroup_tooltipposition': 'eEzsignformfieldgroupTooltipposition',  # noqa: E501
        'a_obj_dropdown_element': 'a_objDropdownElement',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EzsignformfieldgroupRequestCompound - a model defined in OpenAPI

        Keyword Args:
            fki_ezsigndocument_id (FieldPkiEzsigndocumentID):
            e_ezsignformfieldgroup_type (FieldEEzsignformfieldgroupType):
            e_ezsignformfieldgroup_signerrequirement (FieldEEzsignformfieldgroupSignerrequirement):
            s_ezsignformfieldgroup_label (str): The Label for the Ezsignformfieldgroup
            i_ezsignformfieldgroup_step (FieldIEzsignformfieldgroupStep):
            s_ezsignformfieldgroup_defaultvalue (str): The default value for the Ezsignformfieldgroup
            i_ezsignformfieldgroup_filledmin (FieldIEzsignformfieldgroupFilledmin):
            i_ezsignformfieldgroup_filledmax (FieldIEzsignformfieldgroupFilledmax):
            b_ezsignformfieldgroup_readonly (bool): Whether the Ezsignformfieldgroup is read only or not.
            a_obj_ezsignformfieldgroupsigner ([EzsignformfieldgroupsignerRequestCompound]):
            a_obj_ezsignformfield ([EzsignformfieldRequestCompound]):
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
            pki_ezsignformfieldgroup_id (FieldPkiEzsignformfieldgroupID): [optional]  # noqa: E501
            i_ezsignformfieldgroup_maxlength (FieldIEzsignformfieldgroupMaxlength): [optional]  # noqa: E501
            b_ezsignformfieldgroup_encrypted (bool): Whether the Ezsignformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**. [optional]  # noqa: E501
            s_ezsignformfieldgroup_regexp (str): A regular expression to indicate what values are acceptable for the Ezsignformfieldgroup.  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**. [optional]  # noqa: E501
            t_ezsignformfieldgroup_tooltip (str): A tooltip that will be presented to Ezsignsigner about the Ezsignformfieldgroup. [optional]  # noqa: E501
            e_ezsignformfieldgroup_tooltipposition (FieldEEzsignformfieldgroupTooltipposition): [optional]  # noqa: E501
            a_obj_dropdown_element ([CustomDropdownElementRequestCompound]): [optional]  # noqa: E501
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
        """EzsignformfieldgroupRequestCompound - a model defined in OpenAPI

        Keyword Args:
            fki_ezsigndocument_id (FieldPkiEzsigndocumentID):
            e_ezsignformfieldgroup_type (FieldEEzsignformfieldgroupType):
            e_ezsignformfieldgroup_signerrequirement (FieldEEzsignformfieldgroupSignerrequirement):
            s_ezsignformfieldgroup_label (str): The Label for the Ezsignformfieldgroup
            i_ezsignformfieldgroup_step (FieldIEzsignformfieldgroupStep):
            s_ezsignformfieldgroup_defaultvalue (str): The default value for the Ezsignformfieldgroup
            i_ezsignformfieldgroup_filledmin (FieldIEzsignformfieldgroupFilledmin):
            i_ezsignformfieldgroup_filledmax (FieldIEzsignformfieldgroupFilledmax):
            b_ezsignformfieldgroup_readonly (bool): Whether the Ezsignformfieldgroup is read only or not.
            a_obj_ezsignformfieldgroupsigner ([EzsignformfieldgroupsignerRequestCompound]):
            a_obj_ezsignformfield ([EzsignformfieldRequestCompound]):
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
            pki_ezsignformfieldgroup_id (FieldPkiEzsignformfieldgroupID): [optional]  # noqa: E501
            i_ezsignformfieldgroup_maxlength (FieldIEzsignformfieldgroupMaxlength): [optional]  # noqa: E501
            b_ezsignformfieldgroup_encrypted (bool): Whether the Ezsignformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**. [optional]  # noqa: E501
            s_ezsignformfieldgroup_regexp (str): A regular expression to indicate what values are acceptable for the Ezsignformfieldgroup.  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea**. [optional]  # noqa: E501
            t_ezsignformfieldgroup_tooltip (str): A tooltip that will be presented to Ezsignsigner about the Ezsignformfieldgroup. [optional]  # noqa: E501
            e_ezsignformfieldgroup_tooltipposition (FieldEEzsignformfieldgroupTooltipposition): [optional]  # noqa: E501
            a_obj_dropdown_element ([CustomDropdownElementRequestCompound]): [optional]  # noqa: E501
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
              EzsignformfieldgroupRequest,
              EzsignformfieldgroupRequestCompoundAllOf,
          ],
          'oneOf': [
          ],
        }
