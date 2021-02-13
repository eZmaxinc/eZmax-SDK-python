"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign application.  # noqa: E501

    The version of the OpenAPI document: 1.0.30
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eZmaxinc/eZmax-SDK-python.model_utils import (  # noqa: F401
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


class FranchisereferalincomeRequest(ModelNormal):
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

    additional_properties_type = None

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
        return {
            'fki_franchisebroker_id': (int,),  # noqa: E501
            'fki_franchisereferalincomeprogram_id': (int,),  # noqa: E501
            'fki_period_id': (int,),  # noqa: E501
            'd_franchisereferalincome_loan': (str,),  # noqa: E501
            'd_franchisereferalincome_franchiseamount': (str,),  # noqa: E501
            'd_franchisereferalincome_franchisoramount': (str,),  # noqa: E501
            'd_franchisereferalincome_agentamount': (str,),  # noqa: E501
            'dt_franchisereferalincome_disbursed': (str,),  # noqa: E501
            't_franchisereferalincome_comment': (str,),  # noqa: E501
            'fki_franchiseoffice_id': (int,),  # noqa: E501
            's_franchisereferalincome_remoteid': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fki_franchisebroker_id': 'fkiFranchisebrokerID',  # noqa: E501
        'fki_franchisereferalincomeprogram_id': 'fkiFranchisereferalincomeprogramID',  # noqa: E501
        'fki_period_id': 'fkiPeriodID',  # noqa: E501
        'd_franchisereferalincome_loan': 'dFranchisereferalincomeLoan',  # noqa: E501
        'd_franchisereferalincome_franchiseamount': 'dFranchisereferalincomeFranchiseamount',  # noqa: E501
        'd_franchisereferalincome_franchisoramount': 'dFranchisereferalincomeFranchisoramount',  # noqa: E501
        'd_franchisereferalincome_agentamount': 'dFranchisereferalincomeAgentamount',  # noqa: E501
        'dt_franchisereferalincome_disbursed': 'dtFranchisereferalincomeDisbursed',  # noqa: E501
        't_franchisereferalincome_comment': 'tFranchisereferalincomeComment',  # noqa: E501
        'fki_franchiseoffice_id': 'fkiFranchiseofficeID',  # noqa: E501
        's_franchisereferalincome_remoteid': 'sFranchisereferalincomeRemoteid',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, fki_franchisebroker_id, fki_franchisereferalincomeprogram_id, fki_period_id, d_franchisereferalincome_loan, d_franchisereferalincome_franchiseamount, d_franchisereferalincome_franchisoramount, d_franchisereferalincome_agentamount, dt_franchisereferalincome_disbursed, t_franchisereferalincome_comment, fki_franchiseoffice_id, s_franchisereferalincome_remoteid, *args, **kwargs):  # noqa: E501
        """FranchisereferalincomeRequest - a model defined in OpenAPI

        Args:
            fki_franchisebroker_id (int): The unique ID of the Franchisebroker
            fki_franchisereferalincomeprogram_id (int): The unique ID of the Franchisereferalincomeprogram
            fki_period_id (int): The unique ID of the Period
            d_franchisereferalincome_loan (str): The loan amount
            d_franchisereferalincome_franchiseamount (str): The amount that will be given to the franchise
            d_franchisereferalincome_franchisoramount (str): The amount that will be kept by the franchisor
            d_franchisereferalincome_agentamount (str): The amount that will be given to the agent
            dt_franchisereferalincome_disbursed (str): The date the amounts were disbursed
            t_franchisereferalincome_comment (str): A comment about the transaction
            fki_franchiseoffice_id (int): The unique ID of the Franchisereoffice
            s_franchisereferalincome_remoteid (str):

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

        self.fki_franchisebroker_id = fki_franchisebroker_id
        self.fki_franchisereferalincomeprogram_id = fki_franchisereferalincomeprogram_id
        self.fki_period_id = fki_period_id
        self.d_franchisereferalincome_loan = d_franchisereferalincome_loan
        self.d_franchisereferalincome_franchiseamount = d_franchisereferalincome_franchiseamount
        self.d_franchisereferalincome_franchisoramount = d_franchisereferalincome_franchisoramount
        self.d_franchisereferalincome_agentamount = d_franchisereferalincome_agentamount
        self.dt_franchisereferalincome_disbursed = dt_franchisereferalincome_disbursed
        self.t_franchisereferalincome_comment = t_franchisereferalincome_comment
        self.fki_franchiseoffice_id = fki_franchiseoffice_id
        self.s_franchisereferalincome_remoteid = s_franchisereferalincome_remoteid
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
