"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.3
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
)
from ..model_utils import OpenApiModel
from eZmaxApi.exceptions import ApiAttributeError


def lazy_import():
    from eZmaxApi.model.ezsigndocument_request import EzsigndocumentRequest
    from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
    globals()['EzsigndocumentRequest'] = EzsigndocumentRequest
    globals()['FieldPkiLanguageID'] = FieldPkiLanguageID


class EzsigndocumentRequestCompound(ModelComposed):
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
        ('e_ezsigndocument_source',): {
            'BASE64': "Base64",
            'URL': "Url",
        },
        ('e_ezsigndocument_format',): {
            'PDF': "Pdf",
        },
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
            'e_ezsigndocument_source': (str,),  # noqa: E501
            'e_ezsigndocument_format': (str,),  # noqa: E501
            'fki_ezsignfolder_id': (int,),  # noqa: E501
            'dt_ezsigndocument_duedate': (str,),  # noqa: E501
            'fki_language_id': (FieldPkiLanguageID,),  # noqa: E501
            's_ezsigndocument_name': (str,),  # noqa: E501
            's_ezsigndocument_base64': (str,),  # noqa: E501
            's_ezsigndocument_url': (str,),  # noqa: E501
            'b_ezsigndocument_forcerepair': (bool,),  # noqa: E501
            's_ezsigndocument_password': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'e_ezsigndocument_source': 'eEzsigndocumentSource',  # noqa: E501
        'e_ezsigndocument_format': 'eEzsigndocumentFormat',  # noqa: E501
        'fki_ezsignfolder_id': 'fkiEzsignfolderID',  # noqa: E501
        'dt_ezsigndocument_duedate': 'dtEzsigndocumentDuedate',  # noqa: E501
        'fki_language_id': 'fkiLanguageID',  # noqa: E501
        's_ezsigndocument_name': 'sEzsigndocumentName',  # noqa: E501
        's_ezsigndocument_base64': 'sEzsigndocumentBase64',  # noqa: E501
        's_ezsigndocument_url': 'sEzsigndocumentUrl',  # noqa: E501
        'b_ezsigndocument_forcerepair': 'bEzsigndocumentForcerepair',  # noqa: E501
        's_ezsigndocument_password': 'sEzsigndocumentPassword',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EzsigndocumentRequestCompound - a model defined in OpenAPI

        Keyword Args:
            e_ezsigndocument_source (str): Indicates where to look for the document binary content.
            e_ezsigndocument_format (str): Indicates the format of the document.. defaults to "Pdf", must be one of ["Pdf", ]  # noqa: E501
            fki_ezsignfolder_id (int): The unique ID of the Ezsignfolder
            dt_ezsigndocument_duedate (str): The maximum date and time at which the document can be signed.
            fki_language_id (FieldPkiLanguageID):
            s_ezsigndocument_name (str): The name of the document that will be presented to Ezsignfoldersignerassociations
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
            s_ezsigndocument_base64 (str): The Base64 encoded binary content of the document.  This field is Required when eEzsigndocumentSource = Base64.. [optional]  # noqa: E501
            s_ezsigndocument_url (str): The url where the document content resides.  This field is Required when eEzsigndocumentSource = Url.. [optional]  # noqa: E501
            b_ezsigndocument_forcerepair (bool): Try to repair the document or flatten it if it cannot be used for electronic signature. . [optional] if omitted the server will use the default value of True  # noqa: E501
            s_ezsigndocument_password (str): If the source document is password protected, the password to open/modify it.. [optional] if omitted the server will use the default value of ""  # noqa: E501
        """

        e_ezsigndocument_format = kwargs.get('e_ezsigndocument_format', "Pdf")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
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
        """EzsigndocumentRequestCompound - a model defined in OpenAPI

        Keyword Args:
            e_ezsigndocument_source (str): Indicates where to look for the document binary content.
            e_ezsigndocument_format (str): Indicates the format of the document.. defaults to "Pdf", must be one of ["Pdf", ]  # noqa: E501
            fki_ezsignfolder_id (int): The unique ID of the Ezsignfolder
            dt_ezsigndocument_duedate (str): The maximum date and time at which the document can be signed.
            fki_language_id (FieldPkiLanguageID):
            s_ezsigndocument_name (str): The name of the document that will be presented to Ezsignfoldersignerassociations
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
            s_ezsigndocument_base64 (str): The Base64 encoded binary content of the document.  This field is Required when eEzsigndocumentSource = Base64.. [optional]  # noqa: E501
            s_ezsigndocument_url (str): The url where the document content resides.  This field is Required when eEzsigndocumentSource = Url.. [optional]  # noqa: E501
            b_ezsigndocument_forcerepair (bool): Try to repair the document or flatten it if it cannot be used for electronic signature. . [optional] if omitted the server will use the default value of True  # noqa: E501
            s_ezsigndocument_password (str): If the source document is password protected, the password to open/modify it.. [optional] if omitted the server will use the default value of ""  # noqa: E501
        """

        e_ezsigndocument_format = kwargs.get('e_ezsigndocument_format', "Pdf")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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
              EzsigndocumentRequest,
          ],
          'oneOf': [
          ],
        }
