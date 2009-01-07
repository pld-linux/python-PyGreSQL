Summary:	PostgreSQL module for Python
Summary(pl.UTF-8):	Moduł PostgreSQL dla Pythona
Name:		python-PyGreSQL
Version:	4.0
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	ftp://ftp.pygresql.org/pub/distrib/PyGreSQL-%{version}.tgz
# Source0-md5:	1aca50e59ff4cc56abe9452a9a49c5ff
URL:		http://www.pygresql.org/
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
Obsoletes:	python-postgresql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyGreSQL is a Python module that interfaces to a PostgreSQL database.
It embeds the PostgreSQL query library to allow easy use of the
powerful PostgreSQL features from a Python script.

%description -l pl.UTF-8
PyGreSQL to moduł Pythona będący interfejsem do bazy danych
PostgreSQL. Osadza bibliotekę zapytań PostgreSQL, aby umożliwić łatwe
korzystanie z potężnych możliwości PostgreSQL-a w skryptach Pythona.

%prep
%setup -q -n PyGreSQL-%{version}

%build
./setup.py build_ext \
	-I/usr/include/postgresql/server

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install tutorial/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

find $RPM_BUILD_ROOT%{py_sitedir} -type f -name "*.py" -exec rm -rf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{py_sitedir}/_pg.so
%{py_sitedir}/*.py[co]
%{py_sitedir}/PyGreSQL-*.egg-info
%{_examplesdir}/%{name}-%{version}
