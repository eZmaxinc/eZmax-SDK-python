# ListpresentationResponseCompound

A Listpresentation Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_listpresentation_description** | **str** | A descriptive for the list presentation | 
**s_listpresentation_filter** | **str** | The filter to apply to the request to limit results. | 
**s_listpresentation_orderby** | **str** | The order by the user chose | 
**a_s_column_name** | **[str]** | An array of column names that the user chose to bee visible | 
**i_listpresentation_row_max** | **int** | The maximum numbers of results to be returned | 
**i_listpresentation_row_offset** | **int** | The starting element from where to start retrieving the results. For example if you started at iRowOffset&#x3D;0 and asked for iRowMax&#x3D;100, to get the next 100 results, you could specify iRowOffset&#x3D;100&amp;iRowMax&#x3D;100, | 
**b_listpresentation_default** | **bool** | Set to true if the user chose this Listpresentation as the default one. A single element should be set to true | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


