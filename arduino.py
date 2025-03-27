import threading
import random
import time
import dearpygui.dearpygui as dpg

# Liste per memorizzare i dati
dati_temperatura = []
dati_umidita = []
timestamp_temporale = []


def genera_dati():
    """Genera dati casuali di temperatura e umidità per aggiornare i grafici"""
    global dati_temperatura, dati_umidita, timestamp_temporale
    while dpg.is_dearpygui_running():  # Mantiene attiva la generazione dei dati finché la GUI è aperta
        temperatura = random.uniform(20, 23)  # Genera temperatura casuale
        umidita = random.uniform(30, 40)  # Genera umidità casuale
        tempo = len(dati_temperatura)  # Usa l'indice come tempo fittizio

        # Aggiunge i valori alle liste
        dati_temperatura.append(temperatura)
        dati_umidita.append(umidita)
        timestamp_temporale.append(tempo)

        # Mantiene solo gli ultimi 100 punti per evitare sovraccarico
        if len(dati_temperatura) > 100:
            dati_temperatura.pop(0)
            dati_umidita.pop(0)
            timestamp_temporale.pop(0)

        # Aggiorna i grafici
        dpg.set_value("grafico_temperatura", [timestamp_temporale, dati_temperatura])
        dpg.set_value("grafico_umidita", [timestamp_temporale, dati_umidita])
        dpg.set_value("latest_values", f"Temperatura: {temperatura:.1f} °C, Umidità: {umidita:.1f}%")

        time.sleep(1)  # Attende 1 secondo prima di generare nuovi dati


# Configura Dear PyGui
dpg.create_context()
dpg.create_viewport(title='Simulazione Dati Arduino', width=800, height=600)
dpg.setup_dearpygui()

with dpg.window(label="Grafico Dati", width=800, height=600):
    dpg.add_text("Dati in tempo reale simulati")
    dpg.add_text("In attesa di dati...", tag="latest_values")

    # Grafico Temperatura
    with dpg.plot(label="Temperatura", height=400, width=700):
        dpg.add_plot_legend()
        asse_x_temp = dpg.add_plot_axis(dpg.mvXAxis, label="Tempo")
        asse_y_temp = dpg.add_plot_axis(dpg.mvYAxis, label="Temperatura (°C)")
        dpg.set_axis_limits(asse_y_temp, 15, 30)  # Limiti dell'asse Y
        dpg.add_line_series([], [], label="Temperatura °C", parent=asse_y_temp, tag="grafico_temperatura")

    # Grafico Umidità
    with dpg.plot(label="Umidità", height=400, width=700):
        dpg.add_plot_legend()
        asse_x_umid = dpg.add_plot_axis(dpg.mvXAxis, label="Tempo")
        asse_y_umid = dpg.add_plot_axis(dpg.mvYAxis, label="Umidità (%)")
        dpg.set_axis_limits(asse_y_umid, 30, 70)  # Limiti dell'asse Y
        dpg.add_line_series([], [], label="Umidità %", parent=asse_y_umid, tag="grafico_umidita")

# Avvia il thread per generare i dati casuali
thread = threading.Thread(target=genera_dati, daemon=True)
thread.start()

# Mostra la finestra
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
