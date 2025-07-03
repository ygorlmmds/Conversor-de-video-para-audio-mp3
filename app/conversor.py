from moviepy.editor import VideoFileClip
from tkinter import filedialog, messagebox
import imageio_ffmpeg
import os
import traceback


os.environ["FFMPEG_BINARY"] = imageio_ffmpeg.get_ffmpeg_exe()
def converter():
    caminho_video = filedialog.askopenfilename(
        title="Escolha o vídeo", 
        filetypes=[("Arquivos de vídeo", "*.mp4 *.avi *.mov *.mkv")])

    if caminho_video:
        try:
            print(f"Vídeo selecionado: {caminho_video}")
            video = VideoFileClip(caminho_video)

            if not video.audio:
                raise ValueError("O vídeo não possui faixa de áudio.")

            nome_base = os.path.splitext(os.path.basename(caminho_video))[0]
            saida_audio = os.path.join(os.path.dirname(caminho_video), f'{nome_base}.mp3')

            print(f"Salvando áudio em: {saida_audio}")
            video.audio.write_audiofile(saida_audio,verbose=False, logger=None)
            messagebox.showinfo('Sucesso!', f'convertido para:{saida_audio}')

        except Exception:
            with open("erro_log.txt", "w", encoding="utf-8") as f:
                f.write(traceback.format_exc())
            messagebox.showerror(
                "Erro no programa",
                "Ocorreu um erro. Detalhes foram salvos no arquivo erro_log.txt"
            )

    