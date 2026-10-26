import time
from pathlib import Path
from Audio import Audio


def main():
    # Pasta onde está este ficheiro MainAudio.py
    BASE_DIR = Path(__file__).resolve().parent

    # Pasta dos sons
    AUDIO_DIR = BASE_DIR / "resources" / "audio"

    # Caminhos dos ficheiros áudio
    soundtrack = AUDIO_DIR / "super_mario_theme.wav"
    efeito_moeda = AUDIO_DIR / "sonic_ring_effect.wav"
    efeito_fim = AUDIO_DIR / "super_mario_end.wav"
    boss_music = AUDIO_DIR / "winner_ost.wav"

    print("A iniciar teste de áudio...")

    Audio.play_soundtrack(str(soundtrack))

    time.sleep(2)

    print("A tocar efeito sonoro...")
    Audio.play_effect(str(efeito_moeda))

    time.sleep(3)

    if Audio.is_soundtrack_playing():
        print("A soundtrack está a tocar.")

    print("A trocar soundtrack...")
    Audio.change_soundtrack(str(boss_music))

    time.sleep(3)

    print("A tocar efeito final...")
    Audio.play_effect(str(efeito_fim))

    time.sleep(4)

    print("A parar todos os áudios...")
    Audio.stop_all()

    print("Teste terminado.")


if __name__ == "__main__":
    main()