# EzsignfolderSendV1Request

Request for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/send

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t_extra_message** | **str** | A custom text message that will be added to the email sent. | 

## Example

```python
from eZmaxApi.models.ezsignfolder_send_v1_request import EzsignfolderSendV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderSendV1Request from a JSON string
ezsignfolder_send_v1_request_instance = EzsignfolderSendV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignfolderSendV1Request.to_json()

# convert the object into a dict
ezsignfolder_send_v1_request_dict = ezsignfolder_send_v1_request_instance.to_dict()
# create an instance of EzsignfolderSendV1Request from a dict
ezsignfolder_send_v1_request_form_dict = ezsignfolder_send_v1_request.from_dict(ezsignfolder_send_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


