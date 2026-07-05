\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hw}[2023/08/28 Template for 2023-2024 problem sets]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions

\LoadClass[12pt,letterpaper]{article}

\RequirePackage{fullpage,graphicx}
\RequirePackage{amsmath,amsfonts,amsthm,amssymb,multirow,xcolor}
\RequirePackage{algorithmic}
\RequirePackage[ruled,vlined,commentsnumbered,titlenotnumbered]{algorithm2e}
%\RequirePackage{palatino}
\usepackage{newpxtext}
\RequirePackage{etoolbox}
\RequirePackage{verbatim}
\RequirePackage{newpxmath}
\RequirePackage{mdframed}
\RequirePackage{mathtools}
\RequirePackage{enumerate}
\RequirePackage[colorlinks=true,linkcolor=black,urlcolor=black]{hyperref}

\DeclarePairedDelimiter\set{\{}{\}}
\DeclareMathOperator{\poly}{poly}
\DeclareMathOperator{\negl}{negl}
\DeclarePairedDelimiter\inner{\langle}{\rangle}
\DeclarePairedDelimiter\length{\lVert}{\rVert}
\setcounter{MaxMatrixCols}{20}
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cC}{\mathcal{C}}
\newcommand{\F}{\mathbb{F}}

\setcounter{MaxMatrixCols}{20} \setlength\parindent{0pt}

\newcommand{\R}{\mathbb{R}} \newcommand{\calD}{\mathcal{D}}
\newcommand{\A}{\mathcal{A}} \newcommand{\bit}{\{0,1\}}
\newcommand{\keyspace}{\ensuremath{\mathcal{K}}}
\newcommand{\msgspace}{\ensuremath{\mathcal{M}}}
\newcommand{\ctspace}{\ensuremath{\mathcal{C}}}
\newcommand{\tagspace}{\ensuremath{\mathcal{T}}}
\newcommand{\idspace}{\ensuremath{\mathcal{ID}}}
\newcommand{\skcgen}{{\sf Gen}} \newcommand{\skcenc}{{\sf Enc}}
\newcommand{\skcdec}{{\sf Dec}}
\newcommand{\white}{\color{white}} \newcommand{\red}{\color{red}}
\DeclareMathOperator{\polylog}{polylog}
\newcommand{\N}{\mathbb{N}}
\newcommand{\scheme}[1]{\ensuremath{\text{#1}}}
\newcommand{\algo}[1]{\ensuremath{\mathsf{#1}}}
\newcommand{\prg}{\algo{PRG}} \newcommand{\prf}{\algo{PRF}}
\newcommand{\prp}{\algo{PRP}} \newcommand{\skc}{\scheme{SKC}}
\DeclarePairedDelimiter\abs{\lvert}{\rvert}
\newcommand{\concat}{\ensuremath{\|}}
\newcommand{\attacker}[1]{\ensuremath{\mathcal{#1}}}
\newcommand{\Dist}{\attacker{D}} \newcommand{\Ora}{\attacker{O}}
\newcommand{\advan}{\ensuremath{\mathbf{Adv}}}
\newcommand{\mac}{\scheme{MAC}} \newcommand{\macgen}{\algo{Gen}}
\newcommand{\mactag}{\algo{Tag}} \newcommand{\macver}{\algo{Ver}}
\renewcommand{\For}{\attacker{F}}
\newcommand{\Adv}{\attacker{A}}
\newcommand{\sample}{\ensuremath{{\overset{\$}{\leftarrow}}}\xspace}


\newcounter{sheet}

\newcommand{\student}{ YOUR NAME HERE (uniqname here) }
\newcommand{\collaborators}{Name/Exercise Number(s), Name/Exercise
  Numbers(s)}
\newtheorem*{theorem*}{Theorem}

\renewcommand\maketitle{%
\hrule height 1pt
\begin{center}
{\bf \large University of Michigan--Ann Arbor}\\[2mm]
{\small Department of Electrical Engineering and Computer Science}\\[2mm]
EECS 475 \textbf{Introduction to Cryptography}, Fall 2024\\[2mm]
Instructor: Ke Wu\\[1mm]
GSI: Forest Zhang \\[5mm]
\textbf{Homework \arabic{sheet}}
\end{center}
\hrule height 1pt
\begin{center}
  {\bf Student:} \student\\[2mm]
  
  {\bf Collaborators (if any):} \collaborators
\end{center}

\emph{%
%The due date is as indicated on Canvas, Gradescope, and the
%course calendar. 
Please refer to the course information document for important 
collaboration policies. Among other policies, you must list all 
collaborators and, moreover, cite any external resources that 
you have used for each exercise. You must write all solutions 
on your own and may not share this material outside class.}
\\[1mm]
\hrule height 1pt
}

\newcounter{nexercise}

%-----------------------------------------------------------------------------
% Toggle on and off model answers here:
\newtoggle{answers}
\toggletrue{answers}  % True  -> Answers visible
%\togglefalse{answers} % False -> Answers invisible
%-----------------------------------------------------------------------------

\newenvironment{exercise}%
{\stepcounter{nexercise} \subsection*{Exercise \arabic{nexercise}}}%
{\iftoggle{answers}{}{\vspace{5mm}\hrule}}

\newenvironment{answer}%
{\iftoggle{answers}{\subsection*{Solution}\begin{mdframed}[linewidth=1pt]}{\expandafter\comment}}%
{\iftoggle{answers}{\end{mdframed}\vspace{5mm}\hrule}{\expandafter\endcomment}}

\endinput
