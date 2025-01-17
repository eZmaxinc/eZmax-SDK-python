# CustomAttachmentResponse

A Custom Attachment Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_attachment_proof** | [**AttachmentResponseCompound**](AttachmentResponseCompound.md) |  | [optional] 
**obj_attachment_proofdocument** | [**AttachmentResponseCompound**](AttachmentResponseCompound.md) |  | [optional] 
**a_obj_attachment_attachment** | [**List[AttachmentResponseCompound]**](AttachmentResponseCompound.md) |  | [optional] 
**a_obj_attachment_version** | [**List[AttachmentResponseCompound]**](AttachmentResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.custom_attachment_response import CustomAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttachmentResponse from a JSON string
custom_attachment_response_instance = CustomAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(CustomAttachmentResponse.to_json())

# convert the object into a dict
custom_attachment_response_dict = custom_attachment_response_instance.to_dict()
# create an instance of CustomAttachmentResponse from a dict
custom_attachment_response_from_dict = CustomAttachmentResponse.from_dict(custom_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


