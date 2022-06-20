"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.9
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
    from eZmaxApi.model.field_i_ezsignpage_heightimage import FieldIEzsignpageHeightimage
    from eZmaxApi.model.field_i_ezsignpage_heightpdf import FieldIEzsignpageHeightpdf
    from eZmaxApi.model.field_i_ezsignpage_pagenumber import FieldIEzsignpagePagenumber
    from eZmaxApi.model.field_i_ezsignpage_widthimage import FieldIEzsignpageWidthimage
    from eZmaxApi.model.field_i_ezsignpage_widthpdf import FieldIEzsignpageWidthpdf
    from eZmaxApi.model.field_pki_ezsignpage_id import FieldPkiEzsignpageID
    globals()['FieldIEzsignpageHeightimage'] = FieldIEzsignpageHeightimage
    globals()['FieldIEzsignpageHeightpdf'] = FieldIEzsignpageHeightpdf
    globals()['FieldIEzsignpagePagenumber'] = FieldIEzsignpagePagenumber
    globals()['FieldIEzsignpageWidthimage'] = FieldIEzsignpageWidthimage
    globals()['FieldIEzsignpageWidthpdf'] = FieldIEzsignpageWidthpdf
    globals()['FieldPkiEzsignpageID'] = FieldPkiEzsignpageID


class EzsignpageResponse(ModelNormal):
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
            'pki_ezsignpage_id': (FieldPkiEzsignpageID,),  # noqa: E501
            'i_ezsignpage_widthimage': (FieldIEzsignpageWidthimage,),  # noqa: E501
            'i_ezsignpage_heightimage': (FieldIEzsignpageHeightimage,),  # noqa: E501
            'i_ezsignpage_widthpdf': (FieldIEzsignpageWidthpdf,),  # noqa: E501
            'i_ezsignpage_heightpdf': (FieldIEzsignpageHeightpdf,),  # noqa: E501
            'i_ezsignpage_pagenumber': (FieldIEzsignpagePagenumber,),  # noqa: E501
            's_image_url': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pki_ezsignpage_id': 'pkiEzsignpageID',  # noqa: E501
        'i_ezsignpage_widthimage': 'iEzsignpageWidthimage',  # noqa: E501
        'i_ezsignpage_heightimage': 'iEzsignpageHeightimage',  # noqa: E501
        'i_ezsignpage_widthpdf': 'iEzsignpageWidthpdf',  # noqa: E501
        'i_ezsignpage_heightpdf': 'iEzsignpageHeightpdf',  # noqa: E501
        'i_ezsignpage_pagenumber': 'iEzsignpagePagenumber',  # noqa: E501
        's_image_url': 'sImageUrl',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, pki_ezsignpage_id, i_ezsignpage_widthimage, i_ezsignpage_heightimage, i_ezsignpage_widthpdf, i_ezsignpage_heightpdf, i_ezsignpage_pagenumber, s_image_url, *args, **kwargs):  # noqa: E501
        """EzsignpageResponse - a model defined in OpenAPI

        Args:
            pki_ezsignpage_id (FieldPkiEzsignpageID):
            i_ezsignpage_widthimage (FieldIEzsignpageWidthimage):
            i_ezsignpage_heightimage (FieldIEzsignpageHeightimage):
            i_ezsignpage_widthpdf (FieldIEzsignpageWidthpdf):
            i_ezsignpage_heightpdf (FieldIEzsignpageHeightpdf):
            i_ezsignpage_pagenumber (FieldIEzsignpagePagenumber):
            s_image_url (str): The Url to the Ezsignpage's rasterized image.  Url will expire after 5 minutes.

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

        self.pki_ezsignpage_id = pki_ezsignpage_id
        self.i_ezsignpage_widthimage = i_ezsignpage_widthimage
        self.i_ezsignpage_heightimage = i_ezsignpage_heightimage
        self.i_ezsignpage_widthpdf = i_ezsignpage_widthpdf
        self.i_ezsignpage_heightpdf = i_ezsignpage_heightpdf
        self.i_ezsignpage_pagenumber = i_ezsignpage_pagenumber
        self.s_image_url = s_image_url
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
    def __init__(self, pki_ezsignpage_id, i_ezsignpage_widthimage, i_ezsignpage_heightimage, i_ezsignpage_widthpdf, i_ezsignpage_heightpdf, i_ezsignpage_pagenumber, s_image_url, *args, **kwargs):  # noqa: E501
        """EzsignpageResponse - a model defined in OpenAPI

        Args:
            pki_ezsignpage_id (FieldPkiEzsignpageID):
            i_ezsignpage_widthimage (FieldIEzsignpageWidthimage):
            i_ezsignpage_heightimage (FieldIEzsignpageHeightimage):
            i_ezsignpage_widthpdf (FieldIEzsignpageWidthpdf):
            i_ezsignpage_heightpdf (FieldIEzsignpageHeightpdf):
            i_ezsignpage_pagenumber (FieldIEzsignpagePagenumber):
            s_image_url (str): The Url to the Ezsignpage's rasterized image.  Url will expire after 5 minutes.

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

        self.pki_ezsignpage_id = pki_ezsignpage_id
        self.i_ezsignpage_widthimage = i_ezsignpage_widthimage
        self.i_ezsignpage_heightimage = i_ezsignpage_heightimage
        self.i_ezsignpage_widthpdf = i_ezsignpage_widthpdf
        self.i_ezsignpage_heightpdf = i_ezsignpage_heightpdf
        self.i_ezsignpage_pagenumber = i_ezsignpage_pagenumber
        self.s_image_url = s_image_url
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
