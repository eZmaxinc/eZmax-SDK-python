# GlobalEzmaxcustomerGetConfigurationV1Response

Response for GET /1/ezmaxcustomer/{pksEzmaxcustomerCode}/getConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_infrastructureregion_code** | **str** | The region code | 
**s_infrastructureregion_code_web** | **str** | The region code | 
**s_infrastructureenvironmenttype_description** | **str** | The environment type Description | 
**s_cognito_client_id_external** | **str** | The ID of the client in Cognito | [optional] 
**s_cognito_client_id_ezmaxpublic** | **str** | The ID of the client in Cognito | 

## Example

```python
from eZmaxApi.models.global_ezmaxcustomer_get_configuration_v1_response import GlobalEzmaxcustomerGetConfigurationV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalEzmaxcustomerGetConfigurationV1Response from a JSON string
global_ezmaxcustomer_get_configuration_v1_response_instance = GlobalEzmaxcustomerGetConfigurationV1Response.from_json(json)
# print the JSON string representation of the object
print(GlobalEzmaxcustomerGetConfigurationV1Response.to_json())

# convert the object into a dict
global_ezmaxcustomer_get_configuration_v1_response_dict = global_ezmaxcustomer_get_configuration_v1_response_instance.to_dict()
# create an instance of GlobalEzmaxcustomerGetConfigurationV1Response from a dict
global_ezmaxcustomer_get_configuration_v1_response_from_dict = GlobalEzmaxcustomerGetConfigurationV1Response.from_dict(global_ezmaxcustomer_get_configuration_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


