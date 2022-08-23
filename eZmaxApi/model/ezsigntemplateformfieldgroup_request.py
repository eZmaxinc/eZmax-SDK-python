"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.10
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
    from eZmaxApi.model.field_e_ezsigntemplateformfieldgroup_signerrequirement import FieldEEzsigntemplateformfieldgroupSignerrequirement
    from eZmaxApi.model.field_e_ezsigntemplateformfieldgroup_tooltipposition import FieldEEzsigntemplateformfieldgroupTooltipposition
    from eZmaxApi.model.field_e_ezsigntemplateformfieldgroup_type import FieldEEzsigntemplateformfieldgroupType
    from eZmaxApi.model.field_i_ezsigntemplateformfieldgroup_filledmax import FieldIEzsigntemplateformfieldgroupFilledmax
    from eZmaxApi.model.field_i_ezsigntemplateformfieldgroup_filledmin import FieldIEzsigntemplateformfieldgroupFilledmin
    from eZmaxApi.model.field_i_ezsigntemplateformfieldgroup_maxlength import FieldIEzsigntemplateformfieldgroupMaxlength
    from eZmaxApi.model.field_i_ezsigntemplateformfieldgroup_step import FieldIEzsigntemplateformfieldgroupStep
    from eZmaxApi.model.field_pki_ezsigntemplatedocument_id import FieldPkiEzsigntemplatedocumentID
    from eZmaxApi.model.field_pki_ezsigntemplateformfieldgroup_id import FieldPkiEzsigntemplateformfieldgroupID
    globals()['FieldEEzsigntemplateformfieldgroupSignerrequirement'] = FieldEEzsigntemplateformfieldgroupSignerrequirement
    globals()['FieldEEzsigntemplateformfieldgroupTooltipposition'] = FieldEEzsigntemplateformfieldgroupTooltipposition
    globals()['FieldEEzsigntemplateformfieldgroupType'] = FieldEEzsigntemplateformfieldgroupType
    globals()['FieldIEzsigntemplateformfieldgroupFilledmax'] = FieldIEzsigntemplateformfieldgroupFilledmax
    globals()['FieldIEzsigntemplateformfieldgroupFilledmin'] = FieldIEzsigntemplateformfieldgroupFilledmin
    globals()['FieldIEzsigntemplateformfieldgroupMaxlength'] = FieldIEzsigntemplateformfieldgroupMaxlength
    globals()['FieldIEzsigntemplateformfieldgroupStep'] = FieldIEzsigntemplateformfieldgroupStep
    globals()['FieldPkiEzsigntemplatedocumentID'] = FieldPkiEzsigntemplatedocumentID
    globals()['FieldPkiEzsigntemplateformfieldgroupID'] = FieldPkiEzsigntemplateformfieldgroupID


class EzsigntemplateformfieldgroupRequest(ModelNormal):
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
            'fki_ezsigntemplatedocument_id': (FieldPkiEzsigntemplatedocumentID,),  # noqa: E501
            'e_ezsigntemplateformfieldgroup_type': (FieldEEzsigntemplateformfieldgroupType,),  # noqa: E501
            'e_ezsigntemplateformfieldgroup_signerrequirement': (FieldEEzsigntemplateformfieldgroupSignerrequirement,),  # noqa: E501
            's_ezsigntemplateformfieldgroup_label': (str,),  # noqa: E501
            'i_ezsigntemplateformfieldgroup_step': (FieldIEzsigntemplateformfieldgroupStep,),  # noqa: E501
            's_ezsigntemplateformfieldgroup_defaultvalue': (str,),  # noqa: E501
            'i_ezsigntemplateformfieldgroup_filledmin': (FieldIEzsigntemplateformfieldgroupFilledmin,),  # noqa: E501
            'i_ezsigntemplateformfieldgroup_filledmax': (FieldIEzsigntemplateformfieldgroupFilledmax,),  # noqa: E501
            'b_ezsigntemplateformfieldgroup_readonly': (bool,),  # noqa: E501
            'pki_ezsigntemplateformfieldgroup_id': (FieldPkiEzsigntemplateformfieldgroupID,),  # noqa: E501
            'i_ezsigntemplateformfieldgroup_maxlength': (FieldIEzsigntemplateformfieldgroupMaxlength,),  # noqa: E501
            'b_ezsigntemplateformfieldgroup_encrypted': (bool,),  # noqa: E501
            's_ezsigntemplateformfieldgroup_regexp': (str,),  # noqa: E501
            't_ezsigntemplateformfieldgroup_tooltip': (str,),  # noqa: E501
            'e_ezsigntemplateformfieldgroup_tooltipposition': (FieldEEzsigntemplateformfieldgroupTooltipposition,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fki_ezsigntemplatedocument_id': 'fkiEzsigntemplatedocumentID',  # noqa: E501
        'e_ezsigntemplateformfieldgroup_type': 'eEzsigntemplateformfieldgroupType',  # noqa: E501
        'e_ezsigntemplateformfieldgroup_signerrequirement': 'eEzsigntemplateformfieldgroupSignerrequirement',  # noqa: E501
        's_ezsigntemplateformfieldgroup_label': 'sEzsigntemplateformfieldgroupLabel',  # noqa: E501
        'i_ezsigntemplateformfieldgroup_step': 'iEzsigntemplateformfieldgroupStep',  # noqa: E501
        's_ezsigntemplateformfieldgroup_defaultvalue': 'sEzsigntemplateformfieldgroupDefaultvalue',  # noqa: E501
        'i_ezsigntemplateformfieldgroup_filledmin': 'iEzsigntemplateformfieldgroupFilledmin',  # noqa: E501
        'i_ezsigntemplateformfieldgroup_filledmax': 'iEzsigntemplateformfieldgroupFilledmax',  # noqa: E501
        'b_ezsigntemplateformfieldgroup_readonly': 'bEzsigntemplateformfieldgroupReadonly',  # noqa: E501
        'pki_ezsigntemplateformfieldgroup_id': 'pkiEzsigntemplateformfieldgroupID',  # noqa: E501
        'i_ezsigntemplateformfieldgroup_maxlength': 'iEzsigntemplateformfieldgroupMaxlength',  # noqa: E501
        'b_ezsigntemplateformfieldgroup_encrypted': 'bEzsigntemplateformfieldgroupEncrypted',  # noqa: E501
        's_ezsigntemplateformfieldgroup_regexp': 'sEzsigntemplateformfieldgroupRegexp',  # noqa: E501
        't_ezsigntemplateformfieldgroup_tooltip': 'tEzsigntemplateformfieldgroupTooltip',  # noqa: E501
        'e_ezsigntemplateformfieldgroup_tooltipposition': 'eEzsigntemplateformfieldgroupTooltipposition',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, fki_ezsigntemplatedocument_id, e_ezsigntemplateformfieldgroup_type, e_ezsigntemplateformfieldgroup_signerrequirement, s_ezsigntemplateformfieldgroup_label, i_ezsigntemplateformfieldgroup_step, s_ezsigntemplateformfieldgroup_defaultvalue, i_ezsigntemplateformfieldgroup_filledmin, i_ezsigntemplateformfieldgroup_filledmax, b_ezsigntemplateformfieldgroup_readonly, *args, **kwargs):  # noqa: E501
        """EzsigntemplateformfieldgroupRequest - a model defined in OpenAPI

        Args:
            fki_ezsigntemplatedocument_id (FieldPkiEzsigntemplatedocumentID):
            e_ezsigntemplateformfieldgroup_type (FieldEEzsigntemplateformfieldgroupType):
            e_ezsigntemplateformfieldgroup_signerrequirement (FieldEEzsigntemplateformfieldgroupSignerrequirement):
            s_ezsigntemplateformfieldgroup_label (str): The Label for the Ezsigntemplateformfieldgroup
            i_ezsigntemplateformfieldgroup_step (FieldIEzsigntemplateformfieldgroupStep):
            s_ezsigntemplateformfieldgroup_defaultvalue (str): The default value for the Ezsigntemplateformfieldgroup
            i_ezsigntemplateformfieldgroup_filledmin (FieldIEzsigntemplateformfieldgroupFilledmin):
            i_ezsigntemplateformfieldgroup_filledmax (FieldIEzsigntemplateformfieldgroupFilledmax):
            b_ezsigntemplateformfieldgroup_readonly (bool): Whether the Ezsigntemplateformfieldgroup is read only or not.

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
            pki_ezsigntemplateformfieldgroup_id (FieldPkiEzsigntemplateformfieldgroupID): [optional]  # noqa: E501
            i_ezsigntemplateformfieldgroup_maxlength (FieldIEzsigntemplateformfieldgroupMaxlength): [optional]  # noqa: E501
            b_ezsigntemplateformfieldgroup_encrypted (bool): Whether the Ezsigntemplateformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**. [optional]  # noqa: E501
            s_ezsigntemplateformfieldgroup_regexp (str): A regular expression to indicate what values are acceptable for the Ezsigntemplateformfieldgroup.  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**. [optional]  # noqa: E501
            t_ezsigntemplateformfieldgroup_tooltip (str): A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplateformfieldgroup. [optional]  # noqa: E501
            e_ezsigntemplateformfieldgroup_tooltipposition (FieldEEzsigntemplateformfieldgroupTooltipposition): [optional]  # noqa: E501
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

        self.fki_ezsigntemplatedocument_id = fki_ezsigntemplatedocument_id
        self.e_ezsigntemplateformfieldgroup_type = e_ezsigntemplateformfieldgroup_type
        self.e_ezsigntemplateformfieldgroup_signerrequirement = e_ezsigntemplateformfieldgroup_signerrequirement
        self.s_ezsigntemplateformfieldgroup_label = s_ezsigntemplateformfieldgroup_label
        self.i_ezsigntemplateformfieldgroup_step = i_ezsigntemplateformfieldgroup_step
        self.s_ezsigntemplateformfieldgroup_defaultvalue = s_ezsigntemplateformfieldgroup_defaultvalue
        self.i_ezsigntemplateformfieldgroup_filledmin = i_ezsigntemplateformfieldgroup_filledmin
        self.i_ezsigntemplateformfieldgroup_filledmax = i_ezsigntemplateformfieldgroup_filledmax
        self.b_ezsigntemplateformfieldgroup_readonly = b_ezsigntemplateformfieldgroup_readonly
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
    def __init__(self, fki_ezsigntemplatedocument_id, e_ezsigntemplateformfieldgroup_type, e_ezsigntemplateformfieldgroup_signerrequirement, s_ezsigntemplateformfieldgroup_label, i_ezsigntemplateformfieldgroup_step, s_ezsigntemplateformfieldgroup_defaultvalue, i_ezsigntemplateformfieldgroup_filledmin, i_ezsigntemplateformfieldgroup_filledmax, b_ezsigntemplateformfieldgroup_readonly, *args, **kwargs):  # noqa: E501
        """EzsigntemplateformfieldgroupRequest - a model defined in OpenAPI

        Args:
            fki_ezsigntemplatedocument_id (FieldPkiEzsigntemplatedocumentID):
            e_ezsigntemplateformfieldgroup_type (FieldEEzsigntemplateformfieldgroupType):
            e_ezsigntemplateformfieldgroup_signerrequirement (FieldEEzsigntemplateformfieldgroupSignerrequirement):
            s_ezsigntemplateformfieldgroup_label (str): The Label for the Ezsigntemplateformfieldgroup
            i_ezsigntemplateformfieldgroup_step (FieldIEzsigntemplateformfieldgroupStep):
            s_ezsigntemplateformfieldgroup_defaultvalue (str): The default value for the Ezsigntemplateformfieldgroup
            i_ezsigntemplateformfieldgroup_filledmin (FieldIEzsigntemplateformfieldgroupFilledmin):
            i_ezsigntemplateformfieldgroup_filledmax (FieldIEzsigntemplateformfieldgroupFilledmax):
            b_ezsigntemplateformfieldgroup_readonly (bool): Whether the Ezsigntemplateformfieldgroup is read only or not.

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
            pki_ezsigntemplateformfieldgroup_id (FieldPkiEzsigntemplateformfieldgroupID): [optional]  # noqa: E501
            i_ezsigntemplateformfieldgroup_maxlength (FieldIEzsigntemplateformfieldgroupMaxlength): [optional]  # noqa: E501
            b_ezsigntemplateformfieldgroup_encrypted (bool): Whether the Ezsigntemplateformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**. [optional]  # noqa: E501
            s_ezsigntemplateformfieldgroup_regexp (str): A regular expression to indicate what values are acceptable for the Ezsigntemplateformfieldgroup.  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea**. [optional]  # noqa: E501
            t_ezsigntemplateformfieldgroup_tooltip (str): A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplateformfieldgroup. [optional]  # noqa: E501
            e_ezsigntemplateformfieldgroup_tooltipposition (FieldEEzsigntemplateformfieldgroupTooltipposition): [optional]  # noqa: E501
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

        self.fki_ezsigntemplatedocument_id = fki_ezsigntemplatedocument_id
        self.e_ezsigntemplateformfieldgroup_type = e_ezsigntemplateformfieldgroup_type
        self.e_ezsigntemplateformfieldgroup_signerrequirement = e_ezsigntemplateformfieldgroup_signerrequirement
        self.s_ezsigntemplateformfieldgroup_label = s_ezsigntemplateformfieldgroup_label
        self.i_ezsigntemplateformfieldgroup_step = i_ezsigntemplateformfieldgroup_step
        self.s_ezsigntemplateformfieldgroup_defaultvalue = s_ezsigntemplateformfieldgroup_defaultvalue
        self.i_ezsigntemplateformfieldgroup_filledmin = i_ezsigntemplateformfieldgroup_filledmin
        self.i_ezsigntemplateformfieldgroup_filledmax = i_ezsigntemplateformfieldgroup_filledmax
        self.b_ezsigntemplateformfieldgroup_readonly = b_ezsigntemplateformfieldgroup_readonly
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
