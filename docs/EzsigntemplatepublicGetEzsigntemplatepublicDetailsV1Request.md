# EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Request

Request for POST /1/object/ezsigntemplatepublic/getEzsigntemplatepublicDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pks_ezmaxcustomer_code** | **str** | The Ezmaxcustomer code | 
**s_ezsigntemplatepublic_referenceid** | **str** | The referenceid of the Ezsigntemplatepublic | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_request import EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Request from a JSON string
ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_request_instance = EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Request.to_json())

# convert the object into a dict
ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_request_dict = ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_request_instance.to_dict()
# create an instance of EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Request from a dict
ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_request_from_dict = EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Request.from_dict(ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


