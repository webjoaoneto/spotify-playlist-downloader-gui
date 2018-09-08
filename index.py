import sys
import os
import time
import threading

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon, QWindow
from ui.mainwindow import Ui_Iniciar
from ui.tablemodel import SpotifyTableModel
from actions.buscar import SpotifyBusca
from actions.youtube import youtube_search

class App(QMainWindow, Ui_Iniciar):
    res = []
    tbl = object
    changedRow  = pyqtSignal(int, list)

    currentPath = ''

    concurrentThreads    = 0
    maxConcurrentThreads = 2

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.defaults()
        self.connect()

    def defaults( self ):
        self.currentPath = os.path.dirname(os.path.realpath('__file__'))
        self.diretorio.setText( self.currentPath )

    def connect( self ):
        self.btnBuscar.clicked.connect( self.buscar_playlists )
        self.btnEscolherDiretorio.clicked.connect( self.escolher_diretorio )
        self.btnProcessar.clicked.connect( self.processar_fila )
        self.btnLimpar.clicked.connect( self.limpar_fila )


    def limpar_fila( self, el ):
        tbl = SpotifyTableModel( datain=[], headerdata=['Pos', 'Artista', 'Nome', 'CodSpotify', 'Url Youtube', 'Status' ])
        self.tbl = tbl

        self.tabelaResultados.setModel( tbl )

    def escolher_diretorio( self, el ):
        file = str(QFileDialog.getExistingDirectory(self, "Salvar na pasta..."))
        self.diretorio.setText( file )

    def buscar_playlists( self, el ):
        playlistUrl = self.textUrlSpotify.text()


        b = SpotifyBusca()
        res = b.buscar_playlist( playlistUrl )

        self.res = res

        tbl = SpotifyTableModel( datain=res, headerdata=['Pos', 'Artista', 'Nome', 'CodSpotify', 'Url Youtube', 'Status' ])
        self.tbl = tbl

        self.tabelaResultados.setModel( tbl )
 
    def processa_linha( self, i, item ):

        while self.maxConcurrentThreads < self.concurrentThreads:
            print( "%s %s " % ( self.maxConcurrentThreads, self.concurrentThreads ))
            time.sleep( 1 )

        self.concurrentThreads += 1

        data = item

        data[5] = "BUSCANDO YOUTUBE"
        self.changedRow.emit( i, data )

        res = youtube_search( "%s %s" % (item[1], item[2]), 1 )

        data[4] = "https://www.youtube.com/watch?v=" + res
        data[5] = "AGUARDANDO DOWNLOAD"
        
        self.changedRow.emit( i, data )

        os.system( "%s %s -o \"%s\" %s" % 
            ( os.path.join(self.currentPath,  'tools', 'youtube-dl.exe' ),
                '-i --extract-audio --audio-format mp3 --audio-quality 0 ',
                os.path.join( self.diretorio.text(), "%02d-%s.%s" % ( i, '%(title)s', '%(ext)s' ) ),
                "https://www.youtube.com/watch?v=" + res ) )
        
        print( ( "%s %s -o '%s' %s" % 
            ( os.path.join(self.currentPath,  'tools', 'youtube-dl.exe' ),
                '--verbose -v -i --extract-audio --audio-format mp3 --audio-quality 0 ',
                os.path.join( self.diretorio.text(), "%02d-%s.%s" % ( i, '%(title)s', '%(ext)s' ) ),
                "https://www.youtube.com/watch?v=" + res ) ) )
        
        data[5] = "FOI!"
        self.changedRow.emit( i, data )
        self.concurrentThreads -= 1


    def processar( self ):
        self.changedRow.connect( self.tabelaResultados.model().setData )

        for i, item in enumerate( self.tbl.arraydata ):
            t = threading.Thread( target=self.processa_linha, args=(i,item) )
            t.start()

    def processar_fila( self, el ):
        self.processar()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = App()
    
    window.show()
    sys.exit(app.exec_())