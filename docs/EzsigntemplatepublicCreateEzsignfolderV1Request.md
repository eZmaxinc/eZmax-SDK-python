# EzsigntemplatepublicCreateEzsignfolderV1Request

Request for POST /1/object/ezsigntemplatepublic/createEzsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pks_ezmaxcustomer_code** | **str** | The Ezmaxcustomer code | 
**s_ezsigntemplatepublic_referenceid** | **str** | The referenceid of the Ezsigntemplatepublic | 
**a_s_ezsigntemplatesigner_description** | **List[str]** |  | 
**a_obj_ezsignsigner** | [**List[EzsignsignerRequestCompound]**](EzsignsignerRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_create_ezsignfolder_v1_request import EzsigntemplatepublicCreateEzsignfolderV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicCreateEzsignfolderV1Request from a JSON string
ezsigntemplatepublic_create_ezsignfolder_v1_request_instance = EzsigntemplatepublicCreateEzsignfolderV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicCreateEzsignfolderV1Request.to_json())

# convert the object into a dict
ezsigntemplatepublic_create_ezsignfolder_v1_request_dict = ezsigntemplatepublic_create_ezsignfolder_v1_request_instance.to_dict()
# create an instance of EzsigntemplatepublicCreateEzsignfolderV1Request from a dict
ezsigntemplatepublic_create_ezsignfolder_v1_request_from_dict = EzsigntemplatepublicCreateEzsignfolderV1Request.from_dict(ezsigntemplatepublic_create_ezsignfolder_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


