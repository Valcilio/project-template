import os
from pathlib import Path

class Context():
    '''Path control to access any path in this project in any level.'''

    def __init__(self):

        self.found_root = False
        self.cur_path = Path(__file__).parent

    def _set_proj_path(self):
        '''Look for .proj_root to set root project path.
        
        Example:
            If you need to call the root path of this project
            you can call this method and get it, it's generally
            used to combine with other strings to get folders' path.
            Call it like this:

                >>> Context()._set_proj_path()
                /user/template
        
        Return:
            The project's root path.
            '''

        for depth in range(15):
            list_files = os.listdir(self.cur_path)

            # If we don't find .proj_root in list_files, look in the folder 
            # above
            if '.proj_root' not in list_files:
                self.cur_path /= '..'
                continue

            # Solve PROJ_DIR and change var found_root
            PROJ_DIR = self.cur_path.resolve()
            self.found_root = True
            break

        # Check if PROJ_DIR was found
        if not self.found_root:
            raise RuntimeError("Project root folder not found. Please check if "
                            "the file ** .proj_root ** exists."
            )

        return PROJ_DIR

    def get_raw_data_fld(self):
        '''Get the raw data path.

        Example:
            Easily give you the path for the raw data folder for
            saving or loading data to/from there, like above.
            
            >>> Context().get_raw_data_fld()
            /user/template/data/raw

        Return:
            The project's path to save and load raw data.'''

        PROJ_DIR = self._set_proj_path()
        return PROJ_DIR / 'data/raw'

    def get_proc_data_fld(self):
        '''Get the processed data path.

        Example:
            Easily give you the path for the processed data folder for
            saving or loading data to/from there, like above.
            
            >>> Context().get_processed_data_fld()
            /user/template/data/processed

        Return:
            The project's path to save and load processed data.'''

        PROJ_DIR = self._set_proj_path()
        return PROJ_DIR / 'data/processed'
    
    def get_inte_data_fld(self):
        '''Get the interim data path.

        Example:
            Easily give you the path for the interim data folder for
            saving or loading data to/from there, like above.
            
            >>> Context().get_interim_data_fld()
            /user/template/data/interim

        Return:
            The project's path to save and load interim data.'''

        PROJ_DIR = self._set_proj_path()
        return PROJ_DIR / 'data/interim'
    
    def get_ext_data_fld(self):
        '''Get the external data path.

        Example:
            Easily give you the path for the external data folder for
            saving or loading data to/from there, like above.
            
            >>> Context().get_external_data_fld()
            /user/template/data/external

        Return:
            The project's path to save and load external data.'''

        PROJ_DIR = self._set_proj_path()
        return PROJ_DIR / 'data/external'