# EzsigntemplateannotationEditObjectV1Request

Request for PUT /1/object/ezsigntemplateannotation/{pkiEzsigntemplateannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplateannotation** | [**EzsigntemplateannotationRequestCompound**](EzsigntemplateannotationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateannotation_edit_object_v1_request import EzsigntemplateannotationEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateannotationEditObjectV1Request from a JSON string
ezsigntemplateannotation_edit_object_v1_request_instance = EzsigntemplateannotationEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateannotationEditObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplateannotation_edit_object_v1_request_dict = ezsigntemplateannotation_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplateannotationEditObjectV1Request from a dict
ezsigntemplateannotation_edit_object_v1_request_from_dict = EzsigntemplateannotationEditObjectV1Request.from_dict(ezsigntemplateannotation_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


