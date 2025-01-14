# EzsignuserEditObjectV1Request

Request for PUT /1/object/ezsignuser/{pkiEzsignuserID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignuser** | [**EzsignuserRequestCompound**](EzsignuserRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignuser_edit_object_v1_request import EzsignuserEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignuserEditObjectV1Request from a JSON string
ezsignuser_edit_object_v1_request_instance = EzsignuserEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignuserEditObjectV1Request.to_json())

# convert the object into a dict
ezsignuser_edit_object_v1_request_dict = ezsignuser_edit_object_v1_request_instance.to_dict()
# create an instance of EzsignuserEditObjectV1Request from a dict
ezsignuser_edit_object_v1_request_from_dict = EzsignuserEditObjectV1Request.from_dict(ezsignuser_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


