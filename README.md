# Termostato con Arduino e DHT11

Questo progetto consiste nella realizzazione di un termostato basato su **Arduino Uno**, un sensore di temperatura e umidità **DHT11** e un **modulo relè** per il controllo di LED in base alla temperatura rilevata.

## Funzionamento
Il sistema legge la temperatura ambiente tramite il sensore DHT11 e, in base a una soglia impostata, attiva o disattiva il relè per accendere o spegnere dei LED che indicano il livello di temperatura.

## Componenti Utilizzati
- **Arduino Uno** – Microcontrollore per la gestione del sistema
- **DHT11** – Sensore di temperatura e umidità
- **Modulo relè** – Per accendere o spegnere i LED
- **LED** – Indicatori visivi della temperatura

## Caratteristiche
- Lettura in tempo reale della temperatura
- Attivazione e disattivazione automatica dei LED in base alla temperatura
- Possibilità di modificare la soglia di temperatura direttamente dal codice
- Output su monitor seriale per il debug e il monitoraggio
- Grafico di temperatura su python in tempo reale

## Installazione e Utilizzo
1. Collegare i componenti seguendo lo schema dei collegamenti.
2. Caricare il codice su Arduino tramite l'IDE di Arduino.
3. Monitorare il funzionamento tramite il Serial Monitor e i grafici creati dal file python.
4. Modificare la soglia di temperatura nel codice se necessario.
