query_clause = "add staff_table Alex Li,25,134435344,IT,2015‐10‐29"

# column_vals = [ col.strip() for col in query_clause.split("values")[1].split(',')]
column_vals = query_clause.split("values")
print(column_vals)
