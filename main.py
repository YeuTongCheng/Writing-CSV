import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename,"r") as csv_file:
        csv_read=csv.reader(csv_file,delimiter=separator, quotechar=quote)
        for row in csv_read:
            field_list=list(row)
            break
    return field_list


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    with open(filename,"r") as csv_file:
        field_name=[]
        csv_read=csv.DictReader(csv_file,delimiter=separator, quotechar=quote)
        for row in csv_read:
            field_name.append(dict(row))
    return field_name


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    with open(filename,"r") as csv_file:
        dictionary={}
        csv_read=csv.DictReader(csv_file,\
                                delimiter=separator, quotechar=quote)
        for row in csv_read:
            dictionary[row[keyfield]]=row
                  
    return dictionary

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename,"w") as csv_file:
        csv_write=csv.DictWriter(csv_file,fieldnames=fieldnames,delimiter=separator,\
                                quotechar=quote,quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        for row in table:
            csv_write.writerow(row)
