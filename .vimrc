runtime! debian.vim

set nocompatible              " be iMproved, required
filetype off                  " required


set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin('~/.vim/plugins')

Plugin 'VundleVim/Vundle.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'vifm/vifm.vim'
"Plugin 'ryanoasis/vim-devicons'
Plugin 'ap/vim-css-color'            		" Color previews for CSS
Plugin 'tpope/vim-surround'    
Plugin 'scrooloose/nerdtree'			" added nerdtree
Plugin 'vim-python/python-syntax'
Plugin 'vimwiki/vimwiki'

call vundle#end() 

" BASIC CONFIGURATION

filetype plugin indent on
syntax enable
set number
set wildmode=longest,list,full
set encoding=UTF-8
set showmatch		" Show matching brackets.
set ignorecase		" Do case insensitive matching
set smartcase		" Do smart case matching
set mouse=a		" Enable mouse usage (all modes)

"Vertically center documents when in insert mode
autocmd InsertEnter * norm zz

"Use System Clipboard
set clipboard+=unnamedplus

"map leader
let mapleader = ","

"Enable and disable auto comment
map <leader>c :setlocal formatoptions-=cro<CR>
map <leader>C :setlocal formatoptions=cro<CR>

"Eable and disbale auto indentation
map <leader>a :setlocal autoindent<CR>
map <leader>A :setlocal noautoindent<CR>

" VIM AIRLINE THEME
let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
let g:airline_theme='murmur'

" NERD TREE CONFIG
nnoremap <silent> tt :NERDTreeToggle<CR>
let g:NERDTreeDirArrowExpandable = '►'
let g:NERDTreeDirArrowCollapsible = '▼'
let NERDTreeShowLineNumbers=0
let NERDTreeShowHidden=0
let NERDTreeMinimalUI = 1
let g:NERDTreeWinSize=32

" Start NERDTree and put the cursor back in the other window.
autocmd VimEnter * NERDTree | wincmd p

" Exit Vim if NERDTree is the only window left.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() |
    \ quit | endif

" If another buffer tries to replace NERDTree, put it in the other window, and bring back NERDTree.
autocmd BufEnter * if bufname('#') =~ 'NERD_tree_\d\+' && bufname('%') !~ 'NERD_tree_\d\+' && winnr('$') > 1 |
    \ let buf=bufnr() | buffer# | execute "normal! \<C-W>w" | execute 'buffer'.buf | endif

" MANAGING TABS
nnoremap <Tab> gt
nnoremap <S-Tab> gT
nnoremap <silent> <A-n> :tabnew<CR> 
nnoremap <silent> <A-,> :tabmove -<CR>
nnoremap <silent> <A-.> :tabmove +<CR>

" MANAGING SPLITS
set splitbelow splitright

" Remap splits navigation to just ( Ctrl + hjkl)
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

" Keybindings for split resizing
noremap <silent> <A-l> :vertical resize +2<CR>
noremap <silent> <A-h> :vertical resize -2<CR>
noremap <silent> <A-k> :resize +2<CR>
noremap <silent> <A-j> :resize -2<CR>

" The following are commented out as they cause vim to behave a lot
" differently from regular Vi. They are highly recommended though.
"set showcmd		" Show (partial) command in status line.

" Source a global configuration file if available
if filereadable("/etc/vim/vimrc.local")
  source /etc/vim/vimrc.local
endif
