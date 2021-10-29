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
    from eZmaxApi.model.field_e_ezsignfolder_step import FieldEEzsignfolderStep
    from eZmaxApi.model.field_e_ezsignfoldertype_privacylevel import FieldEEzsignfoldertypePrivacylevel
    globals()['FieldEEzsignfolderStep'] = FieldEEzsignfolderStep
    globals()['FieldEEzsignfoldertypePrivacylevel'] = FieldEEzsignfoldertypePrivacylevel


class EzsignfolderListElement(ModelNormal):
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
            'pki_ezsignfolder_id': (int,),  # noqa: E501
            'fki_ezsignfoldertype_id': (int,),  # noqa: E501
            'e_ezsignfoldertype_privacylevel': (FieldEEzsignfoldertypePrivacylevel,),  # noqa: E501
            's_ezsignfoldertype_name_x': (str,),  # noqa: E501
            's_ezsignfolder_description': (str,),  # noqa: E501
            'e_ezsignfolder_step': (FieldEEzsignfolderStep,),  # noqa: E501
            'dt_created_date': (str,),  # noqa: E501
            'dt_ezsignfolder_sentdate': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'dt_due_date': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'i_total_document': (int,),  # noqa: E501
            'i_total_document_edm': (int,),  # noqa: E501
            'i_total_signature': (int,),  # noqa: E501
            'i_total_signature_signed': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pki_ezsignfolder_id': 'pkiEzsignfolderID',  # noqa: E501
        'fki_ezsignfoldertype_id': 'fkiEzsignfoldertypeID',  # noqa: E501
        'e_ezsignfoldertype_privacylevel': 'eEzsignfoldertypePrivacylevel',  # noqa: E501
        's_ezsignfoldertype_name_x': 'sEzsignfoldertypeNameX',  # noqa: E501
        's_ezsignfolder_description': 'sEzsignfolderDescription',  # noqa: E501
        'e_ezsignfolder_step': 'eEzsignfolderStep',  # noqa: E501
        'dt_created_date': 'dtCreatedDate',  # noqa: E501
        'dt_ezsignfolder_sentdate': 'dtEzsignfolderSentdate',  # noqa: E501
        'dt_due_date': 'dtDueDate',  # noqa: E501
        'i_total_document': 'iTotalDocument',  # noqa: E501
        'i_total_document_edm': 'iTotalDocumentEdm',  # noqa: E501
        'i_total_signature': 'iTotalSignature',  # noqa: E501
        'i_total_signature_signed': 'iTotalSignatureSigned',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, pki_ezsignfolder_id, fki_ezsignfoldertype_id, e_ezsignfoldertype_privacylevel, s_ezsignfoldertype_name_x, s_ezsignfolder_description, e_ezsignfolder_step, dt_created_date, dt_ezsignfolder_sentdate, dt_due_date, i_total_document, i_total_document_edm, i_total_signature, i_total_signature_signed, *args, **kwargs):  # noqa: E501
        """EzsignfolderListElement - a model defined in OpenAPI

        Args:
            pki_ezsignfolder_id (int): The unique ID of the Ezsignfolder
            fki_ezsignfoldertype_id (int): The unique ID of the Ezsignfoldertype.
            e_ezsignfoldertype_privacylevel (FieldEEzsignfoldertypePrivacylevel):
            s_ezsignfoldertype_name_x (str): The name of the Ezsignfoldertype in the language of the requester
            s_ezsignfolder_description (str): The description of the Ezsign Folder
            e_ezsignfolder_step (FieldEEzsignfolderStep):
            dt_created_date (str): The date and time at which the object was created
            dt_ezsignfolder_sentdate (bool, date, datetime, dict, float, int, list, str, none_type):
            dt_due_date (bool, date, datetime, dict, float, int, list, str, none_type): The date at which no more signature will be accepted on the folder
            i_total_document (int): The total number of Ezsigndocument in the folder
            i_total_document_edm (int): The total number of Ezsigndocument in the folder that were saved in the edm system
            i_total_signature (int): The total number of signature blocks in all Ezsigndocuments in the folder
            i_total_signature_signed (int): The total number of already signed signature blocks in all Ezsigndocuments in the folder

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
        """

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

        self.pki_ezsignfolder_id = pki_ezsignfolder_id
        self.fki_ezsignfoldertype_id = fki_ezsignfoldertype_id
        self.e_ezsignfoldertype_privacylevel = e_ezsignfoldertype_privacylevel
        self.s_ezsignfoldertype_name_x = s_ezsignfoldertype_name_x
        self.s_ezsignfolder_description = s_ezsignfolder_description
        self.e_ezsignfolder_step = e_ezsignfolder_step
        self.dt_created_date = dt_created_date
        self.dt_ezsignfolder_sentdate = dt_ezsignfolder_sentdate
        self.dt_due_date = dt_due_date
        self.i_total_document = i_total_document
        self.i_total_document_edm = i_total_document_edm
        self.i_total_signature = i_total_signature
        self.i_total_signature_signed = i_total_signature_signed
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
    def __init__(self, pki_ezsignfolder_id, fki_ezsignfoldertype_id, e_ezsignfoldertype_privacylevel, s_ezsignfoldertype_name_x, s_ezsignfolder_description, e_ezsignfolder_step, dt_created_date, dt_ezsignfolder_sentdate, dt_due_date, i_total_document, i_total_document_edm, i_total_signature, i_total_signature_signed, *args, **kwargs):  # noqa: E501
        """EzsignfolderListElement - a model defined in OpenAPI

        Args:
            pki_ezsignfolder_id (int): The unique ID of the Ezsignfolder
            fki_ezsignfoldertype_id (int): The unique ID of the Ezsignfoldertype.
            e_ezsignfoldertype_privacylevel (FieldEEzsignfoldertypePrivacylevel):
            s_ezsignfoldertype_name_x (str): The name of the Ezsignfoldertype in the language of the requester
            s_ezsignfolder_description (str): The description of the Ezsign Folder
            e_ezsignfolder_step (FieldEEzsignfolderStep):
            dt_created_date (str): The date and time at which the object was created
            dt_ezsignfolder_sentdate (bool, date, datetime, dict, float, int, list, str, none_type):
            dt_due_date (bool, date, datetime, dict, float, int, list, str, none_type): The date at which no more signature will be accepted on the folder
            i_total_document (int): The total number of Ezsigndocument in the folder
            i_total_document_edm (int): The total number of Ezsigndocument in the folder that were saved in the edm system
            i_total_signature (int): The total number of signature blocks in all Ezsigndocuments in the folder
            i_total_signature_signed (int): The total number of already signed signature blocks in all Ezsigndocuments in the folder

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
        """

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

        self.pki_ezsignfolder_id = pki_ezsignfolder_id
        self.fki_ezsignfoldertype_id = fki_ezsignfoldertype_id
        self.e_ezsignfoldertype_privacylevel = e_ezsignfoldertype_privacylevel
        self.s_ezsignfoldertype_name_x = s_ezsignfoldertype_name_x
        self.s_ezsignfolder_description = s_ezsignfolder_description
        self.e_ezsignfolder_step = e_ezsignfolder_step
        self.dt_created_date = dt_created_date
        self.dt_ezsignfolder_sentdate = dt_ezsignfolder_sentdate
        self.dt_due_date = dt_due_date
        self.i_total_document = i_total_document
        self.i_total_document_edm = i_total_document_edm
        self.i_total_signature = i_total_signature
        self.i_total_signature_signed = i_total_signature_signed
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
