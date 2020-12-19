set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd
set ruler
set cursorline
set encoding=utf-8
set showmatch
set sw=2
set ts=2
set relativenumber
set linebreak

set laststatus=2
set noshowmode

call plug#begin('~/.vim/plugged')

" Temas

Plug 'morhetz/gruvbox'
" Plug 'safv12/andromeda.vim'

Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" IDE 
Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'leafgarland/typescript-vim'
Plug 'peitalin/vim-jsx-typescript'
Plug 'ap/vim-css-color'

call plug#end()

colorscheme gruvbox
let g:gruvbox_contrast_dark = "hard"
let g:airline_theme='gruvbox'
let g:airline#extensions#tabline#enabled = 1

" colorscheme andromeda
set background=dark
set bg=dark

let NERDTreeQuitOnOpen=1

let mapleader=" "
nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
nmap <Leader>t :sp term://zsh<CR>
map <C-n> :NERDTreeToggle<CR>

set backupcopy=yes

"auto close {
function! s:CloseBracket()
	let line = getline('.')
	if line =~# '^\s*\(struct\|class\|enum\) '
  	return "{\<Enter>};\<Esc>O"
  elseif searchpair('(', '', ')', 'bmn', '', line('.'))
  	" Probably inside a function call. Close it off.
  	return "{\<Enter>});\<Esc>O"
  else
    return "{\<Enter>}\<Esc>O"
  endif
endfunction
inoremap <expr> {<Enter> <SID>CloseBracket()

inoremap (; (<CR>);<C-c>O
inoremap (, (<CR>),<C-c>O
inoremap [; [<CR>];<C-c>O
inoremap [, [<CR>],<C-c>O
tnoremap <Esc> <C-\><C-n>
