# DocumenttypeResponse

A Documenttype Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_documenttype_id** | **int** | The unique ID of the Documenttype | 
**obj_documenttype_name** | [**MultilingualDocumenttypeName**](MultilingualDocumenttypeName.md) |  | 
**e_documenttype_step** | [**ComputedEDocumenttypeStep**](ComputedEDocumenttypeStep.md) |  | 
**s_documenttype_defaultfilename** | **str** | The default filename for the document type | 
**b_documenttype_showagent** | **bool** | Whether the document type should be shown to the agent | 
**b_documenttype_isactive** | **bool** | Whether the documenttype is active or not | 
**b_documenttype_sale** | **bool** | Whether the document type applies to sale transactions | [optional] 
**b_documenttype_rental** | **bool** | Whether the document type applies to rental transactions | [optional] 
**b_documenttype_reference** | **bool** | Whether the document type is a reference document | [optional] 
**b_documenttype_mortgagereference** | **bool** | Whether the document type is a mortgage reference | [optional] 
**b_documenttype_evaluation** | **bool** | Whether the document type applies to evaluation transactions | [optional] 
**b_documenttype_consultation** | **bool** | Whether the document type applies to consultation transactions | [optional] 
**b_documenttype_otherservices** | **bool** | Whether the document type applies to other services | [optional] 
**b_documenttype_foreclosedsale** | **bool** | Whether the document type applies to foreclosed sale transactions | [optional] 
**b_documenttype_commercialfunding** | **bool** | Whether the document type applies to commercial funding transactions | [optional] 
**b_documenttype_canafe** | **bool** | Whether the document type applies to Canafe transactions | [optional] 
**e_documenttype_ezcom** | [**FieldEDocumenttypeEzcom**](FieldEDocumenttypeEzcom.md) |  | [optional] 
**e_documenttype_privacydefault** | [**FieldEDocumenttypePrivacydefault**](FieldEDocumenttypePrivacydefault.md) |  | [optional] 
**e_documenttype_statusdefault** | [**FieldEDocumenttypeStatusdefault**](FieldEDocumenttypeStatusdefault.md) |  | [optional] 
**e_documenttype_salebyowner** | [**FieldEDocumenttypeSalebyowner**](FieldEDocumenttypeSalebyowner.md) |  | [optional] 
**e_documenttype_saledisplaybyrole** | [**FieldEDocumenttypeSaledisplaybyrole**](FieldEDocumenttypeSaledisplaybyrole.md) |  | [optional] 
**e_documenttype_transactiontype** | [**FieldEDocumenttypeTransactiontype**](FieldEDocumenttypeTransactiontype.md) |  | [optional] 
**e_documenttype_repossession** | [**FieldEDocumenttypeRepossession**](FieldEDocumenttypeRepossession.md) |  | [optional] 
**a_fki_inscriptiontype_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.documenttype_response import DocumenttypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeResponse from a JSON string
documenttype_response_instance = DocumenttypeResponse.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeResponse.to_json())

# convert the object into a dict
documenttype_response_dict = documenttype_response_instance.to_dict()
# create an instance of DocumenttypeResponse from a dict
documenttype_response_from_dict = DocumenttypeResponse.from_dict(documenttype_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


