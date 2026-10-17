import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf():
    pdf_path = "Informe_Forense_Rescate_Financiero.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                            rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    
    styles = getSampleStyleSheet()
    
    # Custom styles to guarantee autowrap and clean leading
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1A365D'),
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#2B6CB0'),
        spaceBefore=15,
        spaceAfter=8,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#2D3748'),
        spaceAfter=6
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )
    
    table_hdr_style = ParagraphStyle(
        'TableHdr',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        fontName='Helvetica-Bold',
        textColor=colors.white
    )
    
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#2D3748')
    )

    # Document Header
    story.append(Paragraph("INFORME FORENSE Y PLAN DE RESCATE FINANCIERO RADICAL", title_style))
    story.append(Paragraph("<b>Fecha del Análisis:</b> Octubre 2026<br/><b>Metodología:</b> Auditoría de Datos con Pandas en Python", body_style))
    story.append(Spacer(1, 15))
    
    # Capítulo 1
    story.append(Paragraph("CAPÍTULO 1: AUDITORÍA FORENSE PASO A PASO (8 EJERCICIOS)", h1_style))
    
    ejercicios = [
        ("Ejercicio 1: El Top de Gastos Reales", 
         "Filtrar transacciones cotidianas excluyendo saldos iniciales del pasado.",
         "Los dos mayores dolores reales del bolsillo están identificados: Mercado ($15,679,546 COP) y Gadgets y accesorios ($14,785,311 COP). Estos dos conceptos suman más de 30.4 millones de COP. Gastar casi 15 millones en tecnología y accesorios en medio de una crisis severa es una fuga crítica de capital que debió ir a amortizar pasivos."),
        
        ("Ejercicio 2: El Impacto de lo Inclasificable",
         "Calcular el monto acumulado en transacciones vacías o sin clasificar.",
         "El resultado arrojó un cero absoluto (np.float64(0.0)). Esto demuestra un orden riguroso en tus registros diarios. Todo tu dinero real ejecutado tiene nombre y apellido; no hay fugas fantasma, el dinero se va en decisiones de compra completamente conscientes."),
        
        ("Ejercicio 3: Radiografía de Métodos de Pago",
         "Agrupar y sumar los gastos cotidianos según la cuenta o tarjeta utilizada.",
         "Operas con una altísima dependencia del crédito: TC Visa Davivienda ($23.6M), TC Mastercard Black ($5.3M) y ADDI ($4.3M) canalizan más de $33 millones en consumo corriente. Esto genera una ilusión de liquidez falsa que alimenta deudas con intereses altos. Adicionalmente, quemar $9 millones en efectivo es una zona de alto peligro para el gasto hormiga."),
        
        ("Ejercicio 4: El Índice de Gasto Discrecional",
         "Medir el peso de los lujos y deseos frente al gasto total de supervivencia.",
         "Te gastaste exactamente $20,794,651 COP en lujos (Gadgets, Restaurantes, Estadio, Mecato, Regalos, Apps). Esto representa el 17.46% de tu gasto total real ejecutado. Una quinta parte de tus ingresos se va en deseos que podrías recortar mañana mismo. No te falta sueldo, te sobra estilo de vida para tu nivel de deudas."),
        
        ("Ejercicio 5: El Cruce del Peligro (Financiando Lujos)",
         "Cruzar el subconjunto de gastos de estilo de vida contra los métodos de pago.",
         "De los $20.7 millones gastados en puros lujos, más de $14.5 millones se financiaron con deuda corriente (TC Visa Davivienda $12M, TC Mastercard Black $1.2M y ADDI $1.25M). Comprar placer efímero a cuotas con tasas de usura es un comportamiento autodestructivo. Para colmo, usaste $500.000 del Bolsillo Fondo Tranquilidad para lujos, vaciando tu propia seguridad."),
        
        ("Ejercicio 6: El Calendario del Gasto (Evolución Mensual)",
         "Evaluar de forma cronológica la trayectoria de tus egresos en el año.",
         "Tu crisis no es estática: venías en una espiral acelerada. En enero gastabas $5.5M y tocaste un techo crítico en agosto con $23.3 millones de COP en un solo mes. La caída en septiembre ($10M) y octubre ($6.7M) es tu punto de máxima vulnerabilidad; es el momento exacto para congelar el sistema antes de que la bola de nieve sea impagable."),
        
        ("Ejercicio 7: Días de Peligro Financiero",
         "Extraer el día de la semana para detectar cuándo claudica la fuerza de voluntad.",
         "Tu mayor enemigo en el calendario es el viernes con un acumulado salvaje de $44,801,094 COP (casi el doble de cualquier otro día). El síndrome del fin de semana y la mentalidad de 'me lo merezco' destruyen tu flujo de caja apenas llega el día de descanso. Los martes ocupan el segundo lugar ($20.1M) asociados a débitos directos o picos de ansiedad."),
        
        ("Ejercicio 8: Balance de Emergencia (Ingresos vs. Gastos Netos)",
         "Calcular el flujo de caja neto del año excluyendo saldos iniciales.",
         "Ingresos de $125,101,481 COP vs. Gastos de $121,276,290 COP. Tu consola mostró un superávit aparente de $3,825,191 COP. Esto es un espejismo técnico letal: consumes el 96.9% de lo que entra, y ese margen positivo es ficticio porque tus compras se subsidiaron con tarjetas de crédito y no con dinero real de tu cuenta. Vives al filo de la navaja.")
    ]
    
    for titulo, enunciado, conclusion in ejercicios:
        story.append(Paragraph(f"<b>{titulo}</b>", body_style))
        story.append(Paragraph(f"<i>Objetivo:</i> {enunciado}", body_style))
        story.append(Paragraph(f"<i>Conclusión:</i> {conclusion}", bullet_style))
        story.append(Spacer(1, 4))
        
    story.append(Spacer(1, 10))
    
    # Capítulo 2
    story.append(Paragraph("CAPÍTULO 2: LA MATRIZ PIVOTE Y EL CRÉDITO ESCONDIDO", h1_style))
    story.append(Paragraph("Al ejecutar la instrucción avanzada de Pandas <code>pivot_table(index='Cuenta', columns='Mes')</code> sobre tu DataFrame de pasivos, los números arrojaron luz sobre tu cuenta principal de ahorros:", body_style))
    story.append(Paragraph("• <b>El Rastro de Agosto ($15,000,639 COP):</b> Tu matriz registró una salida gigantesca e inusual en la fila <i>Cuenta Davivienda</i> durante agosto. Ese pico fue la huella digital exacta del desembolso de tu crédito de Libre Inversión por $12 millones, dinero que entró y salió de inmediato para tapar otros huecos, acelerando la bola de nieve.", bullet_style))
    story.append(Paragraph("• <b>El Desfase de Octubre ($3,980,104 COP):</b> Tu app MoneyControl alertaba un descontrol en rojo en la sección bancaria. Pandas reveló que el 100% de esos $3.9M salieron de tu cuenta Davivienda. El desfase ocurre porque tu presupuesto no contempla el costo real indexado de tus deudas fijas (como la Libranza que se debita sola antes de que la veas). Tu cuenta de ahorros está secuestrada por el sistema financiero.", bullet_style))
    
    story.append(Spacer(1, 10))
    
    # Capítulo 3
    story.append(Paragraph("CAPÍTULO 3: ALINEACIÓN DE ETIQUETAS (EXCEL VS. MONEYCONTROL)", h1_style))
    story.append(Paragraph("Para terminar con los reportes en rojo falsos en tu celular, debes unificar las etiquetas y ajustar los techos mensuales exactos calculados en el plan de choque:", body_style))
    
    # Clean and fixed columns table to prevent overlap
    hdr_1 = Paragraph("<b>Categoría Excel / App</b>", table_hdr_style)
    hdr_2 = Paragraph("<b>Presupuesto Mensual</b>", table_hdr_style)
    hdr_3 = Paragraph("<b>Acción de Ajuste y Realidad de Datos</b>", table_hdr_style)
    
    table_data = [[hdr_1, hdr_2, hdr_3]]
    
    rows = [
        ("Mercado", "$1,600,000 COP", "En tu Excel tienes $800.000 quincenales, pero en la App le pusiste un techo de $1.5M. Súbelo a $1.6M para unificar criterios."),
        ("Pago bancos y deudas", "$2,465,000 COP", "Corrige el techo de la App de $2.8M al valor exacto de tus pasivos netos: Libranza ($1,731,796) + ADDI ($556,587) + Libre Inversión ($138,056) + Avance TC ($38,350)."),
        ("Comunicaciones (Claro/Cel)", "$318,000 COP", "Une las filas de Claro ($136K quincenal) y Plan Celular ($23K quincenal) de tu Excel en una sola gran etiqueta mensual en la aplicación."),
        ("Servicios Públicos (EPM)", "$600,000 COP", "En tu Excel proyectas $300.000 quincenales, pero en la App tienes un límite bajo de $430.000. Ajusta la app al consumo real de $600K."),
        ("Moto (Gasolina / Mtto)", "$220,000 COP", "En el Excel tienes $110.000 quincenales. En la App pusiste en exceso $297.000. Bájalo en la app para liberar flujo."),
        ("Estilo de Vida (Fuga de Ocio)", "$1,270,000 COP", "¡El hueco negro! En tu Excel solo tienes filas de $20K para lujos. Pero Pandas demostró que gastas $1.73M al mes en Mecato, Estadio y Restaurantes. Crea esta categoría obligatoria en la app con un tope estricto de $1.27M.")
    ]
    
    for cat, pres, accion in rows:
        table_data.append([
            Paragraph(cat, table_cell_style),
            Paragraph(pres, table_cell_style),
            Paragraph(accion, table_cell_style)
        ])
        
    col_widths = [130, 100, 300] # Total 530 points (perfect for letter with 40 margins)
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2B6CB0')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F7FAFC')]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    
    story.append(t)
    story.append(Spacer(1, 15))
    
    # Capítulo 4
    story.append(Paragraph("CAPÍTULO 4: PLAN DE CHOQUE Y LIQUIDACIÓN ESTRATÉGICA", h1_style))
    story.append(Paragraph("<b>1. Tu salario neto real ajustado:</b> Tus $5,672,837 COP quincenales/mensuales brutos equivalen a un <b>salario neto real de $5,219,010 COP al mes</b> en tu cuenta de ahorros, una vez aplicados los descuentos de ley del 8% (Salud y Pensión). No podemos hacer abonos extraordinarios corrientes a ADDI para no asfixiar el diario.", body_style))
    story.append(Paragraph("<b>2. Destrucción de la idea del carro:</b> Queda completamente enterrada la propuesta de vender la moto y prestar $15 millones adicionales. Tu moto solo tiene 11.400 km en dos años, teletrabajas 4 de 5 días y añadir una séptima deuda corriente destruiría el escaso disponible quincenal de tu nómina.", body_style))
    story.append(Paragraph("<b>3. Movimiento Maestro de Fin de Año ($20,000,000 COP Extra):</b>", body_style))
    story.append(Paragraph("• <b>Inyección de Cesantías ($5,000,000 COP):</b> Retirar los 5 millones y, de forma inmediata en menos de 24 horas, <b>liquidar el 100% de tu deuda en ADDI</b> (tu saldo a cargo es de $1,698,128 COP). El excedente de $3,300,000 COP se inyecta completo como abono extraordinario a la Libre Inversión Davi para bajar su saldo de $12M a menos de $9M. ¡Cancela tu usuario de ADDI el mismo día!", bullet_style))
    story.append(Paragraph("• <b>El Bloque Decembrino ($15,000,000 COP):</b> Para que no pases un desierto de 45 días sin ingresos en enero, vas a separar <b>$5,300,000 COP en un Bolsillo intocable</b> que financiará tus quincenas de enero. Con el resto, liquidas completo el Avance de la TC Visa ($1,526,588 COP) y le inyectas los más de $8 millones restantes directos a capital de la Libre Inversión Davi.", bullet_style))
    story.append(Paragraph("• <b>El Panorama al 1 de Febrero 2027:</b> ADDI liquidada ($0), Avance TC liquidado ($0), cupo de la tarjeta de crédito Davivienda recortado y bloqueado en un máximo de $2 millones, el desierto de enero cruzado con efectivo real y la Libre Inversión reducida a su mínima expresión. Rompes de raíz el ciclo destructivo de los últimos 20 años.", bullet_style))
    
    doc.build(story)
    return pdf_path

pdf_generated = generate_pdf()
print(f"PDF local generado exitosamente: {pdf_generated} (Tamaño: {os.path.getsize(pdf_generated)} bytes)")