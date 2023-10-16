help_dict = {
    'uno':'01','dos':'02','tres':'03','cuatro':'04','cinco':'05','seis':'06','siete':'07','ocho':'08','nueve':'09',
    'diez':'10','once':'11','doce':'12','trece':'13','catorce':'14','quince':'15','dieciseis':'16','dieci seis':'16','diecisiete':'17','dieci siete':'17','dieciocho':'18','dieci ocho':'18','diecinueve':'19','dieci nueve':'19',
    'veinte':'20', 'veintiuno':'21', 'veinti uno':'21', 'veintidos':'22', 'veinti dos':'22', 'veintitres':'23', 'veinti tres':'23','veinticuatro':'24', 'veinti cuatro':'24', 'veinticinco':'25', 'veinti cinco':'25', 'veintiseis':'26', 'veinti seis':'26','veintisiete':'27','veinti siete':'27','veintiocho':'28','veinti ocho':'28', 'veintinueve':'29', 'veinti nueve':'29',
    'treinta':'30', 'treinta y uno':'31', "treintayuno":'31', 'treinta y dos':'32', 'treintaydos':'32','treinta y tres':'33','treinta y tres':'33','treintaytres':'33','treinta y cuatro':'34','treintaycuatro':'34','treinta y cinco':'35','treintaycinco':'35','treinta y seis':'36','treintayseis':'36','treinta y siete':'37','treintaysiete':'37','treinta y ocho':'38','treintayocho':'38','treinta y nueve':'39','treintaynueve':'39',
    'cuarente':'40','cuarenta y uno':'41','cuarentayuno':'41','cuarenta y dos':'42','cuarentaydos':'42','cuarenta y tres':'43','cuarentaytres':'43','cuarenta y cuatro':'44','cuarentaycuatro':'44','cuarenta y cinco':'45','cuarentaycinco':'45','cuarenta y seis':'46','cuarenteyseis':'46','cuarenta y siete':'47','cuarentaysiete':'47','cuarenta y ocho':'48','cuarentayocho':'48','cuarenta y nueve':'49','cuarentaynueve':'49',
    'cincuenta':'50','cincuenta y uno':'51','cincuentayuno':'51','cincuenta y dos':'52','cincuentaydos':'52','cincuenta y tres':'53','cincuentaytres':'53','cincuenta y cuatro':'54','cincuentaycuatro':'54','cincuenta y cinco':'55','cincuentaycinco':'55','cincuenta y seis':'56','cincuentayseis':'56','cincuenta y siete':'57','cincuentaysiete':'57','cincuenta y ocho':'58','cincuentayocho':'58','cincuenta y nueve':'59','cincuentaynueve':'59',
    'sesenta':'60','sesenta y uno':'61','sesentayuno':'61','sesenta y dos':'62','sesentaydos':'62','sesenta y tres':'63','sesentaytres':'63','sesenta y cuatro':'64','sesentaycuatro':'64','sesenta y cinco':'65','sesentaycinco':'65','sesenta y seis':'66','sesentayseis':'66','sesenta y siete':'67','sesentaysiete':'67','sesenta y ocho':'68','sesentayocho':'68','sesenta y nueve':'69','sesentaynueve':'69',
    'setenta':'70','setenta y uno':'71','setentayuno':'71','setenta y dos':'72','setentaydos':'72','setenta y tres':'73','setentaytres':'73','setenta y cuatro':'74','setentaycuatro':'74','setenta y cinco':'75','setentaycinco':'75','setenta y seis':'76','setentayseis':'76','setenta y siete':'77','setentaysiete':'77','setenta y ocho':'78','setentayocho':'78','setenta y nueve':'79','setentaynueve':'79',
    'ochenta':'80','ochenta y uno':'81','ochentayuno':'81','ochenta y dos':'82','ochentaydos':'82','ochenta y tres':'83','ochentaytres':'83','ochenta y cuatro':'84','ochentaycuatro':'84','ochenta y cinco':'85','ochentaycinco':'85','ochenta y seis':'86','ochentayseis':'86','ochenta y siete':'87','ochentaysiete':'87','ochenta y ocho':'88','ochentayocho':'88','ochenta y nueve':'89','ochentaynueve':'89',
    'noventa':'90','noventa y uno':'91','noventayuno':'91','noventa y dos':'92','noventaydos':'92','noventa y tres':'93','noventaytres':'93','noventa y cuatro':'94','noventaycuatro':'94','noventa y cinco':'95','noventaycinco':'95','noventa y seis':'96','noventayseis':'96','noventa y siete':'97','noventaysiete':'97','noventa y ocho':'98','noventayocho':'98','noventa y nueve':'99','noventaynueve':'99',
    'cien':'100',
    'ciento':'1',
    'dos cientos':'2','doscientos':'2',
    'tres cientos':'3','trescientos':'3',
    'cuatro cientos':'4','cuatrocientos':'4',
    'quinientos':'5',
    'seis cientos':'6','seiscientos':'6',
    'sete cientos':'7','setecientos':'7',
    'ocho cientos':'8','ochocientos':'8',
    'nove cientos':'9','novecientos':'9',
    'mil':'1000',
    'cero' : '0'
}

def get_number_from_sentence(sentence: str) -> str:
    # Separa la oración en palabras
    words = sentence.split()
    
    updated_words = []  # Lista para almacenar las palabras actualizadas
    
    for word in words:
        # Si la palabra está en el diccionario, obtiene su valor
        updated_word = help_dict.get(word.lower(), word)
        updated_words.append(str(updated_word))
    
    # Une las palabras actualizadas para formar la oración con números reemplazados
    updated_sentence = ' '.join(updated_words)
    
    return updated_sentence