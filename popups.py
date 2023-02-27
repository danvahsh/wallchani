from tkinter.messagebox import showinfo, showwarning, showerror, askretrycancel, _show # type: ignore

def info(title='Sucess!', message='Your photos have been added sucessfully.'):
    return _show(title, message, INFO, OK)


def warn(title='Warning!', message=None):
    return response


def warn_ask(title='Warning!', message='You have chosen a lot of files!\nWould you like to proceed?'):
    return _show(title, message, "warning", "yesno")


if __name__ == '__main__':
    info()
    warn()
    warn_ask()
