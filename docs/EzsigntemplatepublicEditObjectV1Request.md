# EzsigntemplatepublicEditObjectV1Request

Request for PUT /1/object/ezsigntemplatepublic/{pkiEzsigntemplatepublicID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatepublic** | [**EzsigntemplatepublicRequestCompound**](EzsigntemplatepublicRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_edit_object_v1_request import EzsigntemplatepublicEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicEditObjectV1Request from a JSON string
ezsigntemplatepublic_edit_object_v1_request_instance = EzsigntemplatepublicEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicEditObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatepublic_edit_object_v1_request_dict = ezsigntemplatepublic_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatepublicEditObjectV1Request from a dict
ezsigntemplatepublic_edit_object_v1_request_from_dict = EzsigntemplatepublicEditObjectV1Request.from_dict(ezsigntemplatepublic_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


