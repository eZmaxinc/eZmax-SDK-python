# CommonResponseErrorSTemporaryFileUrl

Generic Error Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_temporary_file_url** | **str** | The Temporary File Url of the document that was uploaded. That url can be reused instead of uploading the file again. | [optional] 

## Example

```python
from eZmaxApi.models.common_response_error_s_temporary_file_url import CommonResponseErrorSTemporaryFileUrl

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseErrorSTemporaryFileUrl from a JSON string
common_response_error_s_temporary_file_url_instance = CommonResponseErrorSTemporaryFileUrl.from_json(json)
# print the JSON string representation of the object
print(CommonResponseErrorSTemporaryFileUrl.to_json())

# convert the object into a dict
common_response_error_s_temporary_file_url_dict = common_response_error_s_temporary_file_url_instance.to_dict()
# create an instance of CommonResponseErrorSTemporaryFileUrl from a dict
common_response_error_s_temporary_file_url_from_dict = CommonResponseErrorSTemporaryFileUrl.from_dict(common_response_error_s_temporary_file_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


