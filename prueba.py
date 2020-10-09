trace = "1&0&00&00&00&0&00"
trace = trace.split('&')

data = ["sitio", "velPromedio", "cantExcesos","riezgoPeatonVehiculo","humedadVia","na1","na2"]

trace_dictionary = dict(zip(data,trace))

print(trace_dictionary)


