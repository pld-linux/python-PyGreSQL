
%define module PyGreSQL
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)
%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile python -c "import compileall; compileall.compile_dir('.')"

Summary:       Python interface to PostgresSQL 
Summary(pl):   Interfejs pomiêdzy jêzykiem Python a baz± danych PostgresSQL 
Name:          python-PyGreSQL
Release:       1
Version:       3.1
Copyright:     See description
Group:         Applications/Databases/Interfaces
Group(pl):     Aplikacje/Bazy Danych/Interfejsy
Source:        ftp://ftp.druid.net/pub/distrib/%{module}-%{version}.tgz
Source1:       python-Makefile.pre.in
Source2:       Setup.in.PyGreSQL
URL:           http://www.druid.net/pygresql
BuildRoot:     %{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:      python >= 1.5
BuildRequires: python-devel >= 1.5
BuildRequires: postgresql-devel >= 6.5.3

%description
This package provides access to PostgresSQL data from Python

Written by D'Arcy J.M. Cain, darcy@druid.net
Based heavily on code written by Pascal Andre, andre@chimay.via.ecp.fr.
Copyright (c) 1995, Pascal ANDRE (andre@via.ecp.fr)    

See documentation for the full Copyright notice.

%description -l pl
Ten pakiet zapewnia dostêp do baz danych PostgreSQL z poziomu skryptów
jêzyka Python.

Autor: D'Arcy J.M. Cain, darcy@druid.net
Oparte na kodzie napisanym przez Pascala Andre, andre@chimay.via.ecp.fr.
Copyright (c) 1995, Pascal ANDRE (andre@via.ecp.fr)

Pe³na informacja na temat praw autorskich znajduje siê w dokumentacji.

%prep
%setup -n PyGreSQL-3.1
cp $RPM_SOURCE_DIR/python-Makefile.pre.in ./Makefile.pre.in
cp $RPM_SOURCE_DIR/Setup.in.PyGreSQL Setup.in

%build
%{__make} -f Makefile.pre.in boot
%{__make} OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}
echo %{module} > $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}.pth

%python_compile_opt
%python_compile

install -m 644 pg.py{c,o} $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}
install -m 755 _pgmodule.so $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}

gzip README README.linux Announce ChangeLog
tar czf tutorial.tar.gz tutorial

%files
%defattr(644,root,root,755)
%doc {README,README.linux,tutorial.tar,Announce,ChangeLog}.gz
%attr(755,root,root) %{python_sitepkgsdir}/%{module}/_pgmodule.so
%attr(644,root,root) %{python_sitepkgsdir}/%{module}/*.pyc
%attr(644,root,root) %{python_sitepkgsdir}/%{module}/*.pyo
%attr(644,root,root) %{python_sitepkgsdir}/%{module}.pth
