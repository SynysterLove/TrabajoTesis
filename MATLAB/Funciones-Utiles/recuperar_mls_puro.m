function [x_mls, y_mls] = recuperar_mls_puro(x, y, fs, frecuencia_senoide, cant_periodos_senoide, tiempo_silencio)

    lag = finddelay(x,y); %Computa el delay exacto entre el comienzo de cada se�al
    y_align = y(lag+1:end); %Eliminamos la parte nula al principio de la se�al grabada
    x_align = x(1:end-lag); %Eliminamos la parte sobrante al final de la se�al generada, que no tendr� correspondencia con ninguna parte de la se�al grabada

    %Eliminaci�n de la senoide
    tiempo_senoide = (1/frecuencia_senoide)*cant_periodos_senoide; %Duracion de la senoide
    muestras_senoide = tiempo_senoide*fs; %Cantidad de muestras que conforman la senoide
    x_sin_senoide = x_align(muestras_senoide+1:end);
    y_sin_senoide = y_align(muestras_senoide+1:end);
    
    %Eliminaci�n del silencio
    muestras_silencio = tiempo_silencio*fs;
    x_mls = x_sin_senoide(muestras_silencio+1:end);
    y_mls = y_sin_senoide(muestras_silencio+1:end);

    