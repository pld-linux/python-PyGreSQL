
%define pp_subname PyGreSQL

Summary:       Python interface to PostgresSQL 
Summary(pl):   Interfejs pomiêdzy jêzykiem Python a baz± danych PostgresSQL 
Name:          python-PyGreSQL
Release:       1
Version:       2.4
Copyright:     See description
Group:         Applications/Databases/Interfaces
Group(pl):     Aplikacje/Bazy Danych/Interfejsy
Source:        PyGreSQL.tgz
Source1:       python-Makefile.pre.in
Source2:       Setup.in.PyGreSQL
URL:           http://www.druid.net/pygresql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:      python >= 1.5

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
%setup -n PyGreSQL-2.4
cp $RPM_SOURCE_DIR/python-Makefile.pre.in ./Makefile.pre.in
cp $RPM_SOURCE_DIR/Setup.in.PyGreSQL Setup.in

%build
make -f Makefile.pre.in boot
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
echo %{pp_subname} > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}.pth
install -m 644 pg.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
#install -m 644 pgext.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
install -m 755 _pgmodule.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}

gzip README README.linux Announce ChangeLog
tar czf tutorial.tar.gz tutorial

%files
%defattr(644,root,root,755)
%doc {README,README.linux,tutorial.tar,Announce,ChangeLog}.gz
%attr(755,root,root) %{_libdir}/python1.5/site-packages/%{pp_subname}/_pgmodule.so
#%attr(644,root,root) %{_libdir}/python1.5/site-packages/%{pp_subname}/pgext.py
%attr(644,root,root) %{_libdir}/python1.5/site-packages/%{pp_subname}/pg.py
%attr(644,root,root) %{_libdir}/python1.5/site-packages/%{pp_subname}.pth
